from abc import ABC,abstractmethod
from app.core.model.embedding_model import EmbeddingModel
from app.core.model.search_result_vDB import SearchResult

class VectorStoreInterface(ABC):
    @abstractmethod
    def add_embeddings(self,embeddings:list[EmbeddingModel])-> None:
        pass
    @abstractmethod
    def search(self,query_vector:list[float],k:int)->list[SearchResult]:
        pass
    