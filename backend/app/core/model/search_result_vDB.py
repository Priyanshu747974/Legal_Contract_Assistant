from dataclasses import dataclass 
from app.core.model.embedding_model import EmbeddingModel      

@dataclass
class SearchResult:
    embedding: EmbeddingModel
    score: float