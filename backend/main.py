from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models import ChatRequest, ChatResponse, Message
import os

app = FastAPI(title="TheraMood AI API")

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
    
    # Mock response for now
    # In a real implementation, we would call OpenAI API here
    
    response_text = f"[{emotion} Mode] I hear you saying: '{request.message}'. Tell me more about that."
    
    return ChatResponse(message=response_text)
