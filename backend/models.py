from pydantic import BaseModel
from typing import List, Optional

class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    emotion: str
    message: str
    history: List[Message] = []

class ChatResponse(BaseModel):
    message: str
