# pyrefly: ignore [missing-import]
from fastapi import APIRouter, File, HTTPException, UploadFile
from app.dependencies import rag_service
from app.schemas import QuestionRequest, QuestionResponse
import shutil
import os
from app.dependencies import (
    parser,
    chunker,
    embedder,
    vector_store
)
from app.dependencies import ingestion_service

router = APIRouter()
@router.get("/")
def home():
    return {
        "message": "Legal Contract Assistant API is running"
    }

@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )

    os.makedirs("uploads", exist_ok=True)

    file_path = os.path.join("uploads", file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    chunk_count = ingestion_service.ingest(file_path)

    return {
        "message": "Document indexed successfully.",
        "chunks": chunk_count
    }

@router.post("/ask", response_model=QuestionResponse)
def ask_question(request: QuestionRequest):

    answer = rag_service.generate_answer(request.question)

    return QuestionResponse(
        answer=answer
    )