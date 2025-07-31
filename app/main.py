from fastapi import FastAPI, HTTPException, Path, Query
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime, timezone

app = FastAPI()

# Using In-memory storage as per the project requirements, No Database usage
session_store = []
chat_store = {}

# Creating Pydantic models to support validation using BaseModel
class SessionCreate(BaseModel):
    session_user: str = Field(..., min_length=1)

class SessionResponse(BaseModel):
    session_id: int
    session_user: str
    created_at: str

class Message(BaseModel):
    role: str
    content: str

# Endpoint 1: Creating a new chat session
@app.post("/sessions", response_model=SessionResponse)
def create_session(session: SessionCreate):
    normalised_username = session.session_user.strip().lower()
    if not normalised_username:
        raise HTTPException(status_code=400, detail="Username cannot be empty.")
    session_id = len(session_store) + 1
    created_at = datetime.now(timezone.utc)
    new_session = {
        "session_id": session_id,
        "session_user": normalised_username,
        "created_at": created_at
    }
    session_store.append(new_session)
    chat_store[session_id] = []
    return new_session

# Endpoint 2: Adding a message to session
@app.post("/sessions/{session_id}/messages")
def add_message(session_id: int = Path(..., ge=1), message: Message = ...):
    if session_id not in chat_store:
        raise HTTPException(status_code=404, detail="Session not found.")
    if message.role not in ["user", "assistant"]:
        raise HTTPException(status_code=400, detail="Invalid role. Must be 'user' or 'assistant'.")
    chat_store[session_id].append({"role": message.role, "content": message.content})
    return {"status": "Message added successfully"}

# Endpoint 3: Retrieving all the messages from the session
@app.get("/sessions/{session_id}/messages")
def get_messages(session_id: int = Path(..., ge=1), role: Optional[str] = Query(None)):
    if session_id not in chat_store:
        raise HTTPException(status_code=404, detail="Session not found.")
    messages = chat_store[session_id]
    if role:
        if role not in ["user", "assistant"]:
            raise HTTPException(status_code=400, detail="Invalid role filter.")
        messages = [msg for msg in messages if msg["role"] == role]
    return messages