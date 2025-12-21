from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models import ChatRequest, ChatResponse, Message
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from the root directory (development only)
if os.path.exists("../.env"):
    load_dotenv(dotenv_path="../.env")

app = FastAPI(title="TheraMood AI API")

# Initialize OpenAI client for Groq (expects env var GROQ_API_KEY)
# Note: The user provided a key starting with 'gsk_', which is a Groq API key.
_groq_key = os.getenv("GROQ_API_KEY") or os.getenv("OPENAI_API_KEY")
if _groq_key:
    try:
        client = OpenAI(
            base_url="https://api.groq.com/openai/v1",
            api_key=_groq_key,
        )
    except Exception:
        # If client construction fails, keep client as None and let handlers fallback
        client = None
else:
    client = None

# Debug endpoint (non-sensitive): reports whether GROQ/OPENAI env vars exist and whether the client was constructed.
# This endpoint does NOT return secret values, only presence and whether a quick test call succeeded (when `do_call=true`).
from typing import Optional

@app.get("/debug")
async def debug(do_call: Optional[bool] = False):
    info = {
        "has_groq_env": bool(os.getenv("GROQ_API_KEY")),
        "has_openai_env": bool(os.getenv("OPENAI_API_KEY")),
        "client_initialized": client is not None,
    }

    if do_call:
        if client is None:
            info["test_call"] = "skipped: client not initialized"
        else:
            try:
                # Small/cheap test: request a 1-token completion; may still consume credits
                completion = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[{"role": "user", "content": "hi"}],
                    max_tokens=1,
                )
                info["test_call"] = "success"
            except Exception as e:
                info["test_call"] = f"error: {e}"

    # Allow running locally with `python main.py`
    return info


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 10000)),
    )

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

CRISIS_KEYWORDS = ["suicide", "kill myself", "end it all", "hurt myself", "die"]

SYSTEM_PROMPTS = {
    "Happy": "You are a supportive friend. The user is happy. Celebrate with them and ask what made them feel this way.",
    "Sad": "You are an empathetic listener. The user is sad. Validate their feelings and gently ask about what's wrong. Use reflective listening.",
    "Angry": "You are a calm and non-judgmental presence. The user is angry. Allow them to vent and help them de-escalate. Validate their frustration.",
    "Overwhelmed": "You are a grounding presence. The user is overwhelmed. Help them break down their stressors and breathe. Focus on one thing at a time.",
    "Depressed": "You are a compassionate and gentle companion. The user is feeling depressed. Offer presence and validation. Do not try to 'fix' it immediately, just be there.",
    "Describe": "You are a neutral, open-minded listener. The user wants to describe their feelings. Help them articulate their emotions."
}

@app.get("/")
async def root():
    return {"message": "Welcome to TheraMood AI API"}

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    # Crisis Detection
    if any(keyword in request.message.lower() for keyword in CRISIS_KEYWORDS):
        return ChatResponse(message="I'm concerned about what you're saying. If you are in immediate danger, please call emergency services or a crisis hotline immediately. I am an AI and cannot provide emergency help.")

    emotion = request.emotion
    system_prompt = SYSTEM_PROMPTS.get(emotion, SYSTEM_PROMPTS["Describe"])
    
    try:
        # Construct messages for OpenAI
        messages = [{"role": "system", "content": system_prompt}]
        
        # Add history if available
        for msg in request.history:
            messages.append({"role": msg.role, "content": msg.content})
            
        # Add current user message
        messages.append({"role": "user", "content": request.message})

        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages
        )
        
        response_text = completion.choices[0].message.content
        return ChatResponse(message=response_text)
        
    except Exception as e:
        print(f"Error calling OpenAI: {e}")
        # Fallback to mock response if API fails
        return ChatResponse(message=f"[{emotion} Mode] (Offline) I hear you saying: '{request.message}'. Tell me more about that.")
