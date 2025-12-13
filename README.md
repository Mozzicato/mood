# TheraMood AI

TheraMood AI is a therapist-style chatbot that helps users explore their emotions through guided, empathetic conversation.

## Features

- **Emotion Selection**: Choose from Happy, Sad, Angry, Overwhelmed, Depressed, or Describe.
- **Therapist-Style Chat**: The AI adapts its persona based on the selected emotion.
- **Crisis Detection**: Basic keyword detection to provide safety resources.

## Tech Stack

- **Frontend**: Next.js, Tailwind CSS
- **Backend**: FastAPI, Python
- **AI**: Mocked response (ready for OpenAI integration)

## Setup

### Backend

1. Navigate to `backend/`:
   ```bash
   cd backend
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the server:
   ```bash
   uvicorn main:app --reload
   ```

### Frontend

1. Navigate to `frontend/`:
   ```bash
   cd frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Run the development server:
   ```bash
   npm run dev
   ```

## License

MIT