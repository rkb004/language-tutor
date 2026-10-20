
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
from uuid import uuid4

from app.services.tutor import TeluguTutor
from app.services.memory import ConversationMemory

app = FastAPI(
    title="Telugu Language Tutor",
    description="Local AI-powered conversational Telugu tutor",
    version="0.1.0"
)

tutor = TeluguTutor()
memory = ConversationMemory()


class ChatRequest(BaseModel):
    message: str = Field(min_length=1, max_length=2000)
    session_id: Optional[str] = None
    difficulty: str = "beginner"


class ChatResponse(BaseModel):
    response: str
    session_id: str
    difficulty: str


@app.get("/")
def root():
    return {
        "project": "Telugu Language Tutor",
        "version": "0.1.0",
        "status": "prototype"
    }


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    if request.difficulty not in {
        "beginner", "intermediate", "advanced"
    }:
        raise HTTPException(
            status_code=400,
            detail="Invalid difficulty level"
        )

    session_id = request.session_id or str(uuid4())

    history = memory.get_history(session_id)

    try:
        response = tutor.generate_response(
            message=request.message,
            history=history,
            difficulty=request.difficulty
        )
    except Exception as exc:
        raise HTTPException(
            status_code=503,
            detail=f"Local model unavailable: {exc}"
        )

    memory.add_message(
        session_id, "user", request.message
    )
    memory.add_message(
        session_id, "assistant", response
    )

    return ChatResponse(
        response=response,
        session_id=session_id,
        difficulty=request.difficulty
    )


@app.get("/history/{session_id}")
def get_history(session_id: str):
    return {
        "session_id": session_id,
        "messages": memory.get_history(session_id)
    }


@app.delete("/history/{session_id}")
def clear_history(session_id: str):
    memory.clear(session_id)
    return {"message": "Session cleared"}

