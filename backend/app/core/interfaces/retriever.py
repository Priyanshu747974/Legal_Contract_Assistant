from abc import ABC,abstractmethod
from app.core.model.search_result_vDB import SearchResult

class RetrieverInterface(ABC):
    @abstractmethod
    def retrieve(self, query:str,k:int)->list[SearchResult]:
        pass
