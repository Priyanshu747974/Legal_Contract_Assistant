# pyrefly: ignore [missing-import]
from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="Legal Contract Assistant API",
    version="1.0.0",
    description="Upload legal contracts and ask questions using Retrieval-Augmented Generation (RAG)."
)

app.include_router(router)