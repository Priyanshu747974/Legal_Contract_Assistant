from app.core.model.chunk import Chunk
from abc import ABC,abstractmethod
from app.core.model.embedding_model import EmbeddingModel

class TransformerEmbeddingInterface(ABC):
    @abstractmethod
    def embed_chunks(self,chunk:list[Chunk])->list[EmbeddingModel]:
        pass

    @abstractmethod
    def embed_query(self, query: str) -> list[float]:
        pass
