from dataclasses import dataclass, field
from app.core.model.chunk import Chunk

@dataclass
class EmbeddingModel:
    chunk: Chunk
    vector: list[float]