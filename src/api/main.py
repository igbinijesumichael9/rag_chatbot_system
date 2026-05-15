from fastapi import FastAPI

from src.api.schemas import (
    ChatRequest,
    ChatResponse
)

from src.llm.rag_chain import RAGChatbot


app = FastAPI(
    title="RAG Chatbot API",
    version="1.0.0"
)

chatbot = RAGChatbot()


@app.get("/")
def home():

    return {
        "message": "RAG Chatbot API is running"
    }


@app.post("/chat")
def chat(request: ChatRequest):

    result = chatbot.generate_response(request.query)

    return {
        "question": request.query,
        "answer": result["answer"],
        "sources": result["sources"]
    }