from fastapi import FastAPI
from pydantic import BaseModel

from backend.rag import ask_rag


app = FastAPI(
    title="Mini RAG API"
)


class QuestionRequest(BaseModel):
    question: str


@app.get("/")
def home():
    return {
        "message": "Mini RAG API is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/ask")
def ask_question(request: QuestionRequest):

    answer = ask_rag(request.question)

    return {
        "question": request.question,
        "answer": answer
    }