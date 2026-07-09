from app.core.model.search_result_vDB import SearchResult
from abc import ABC,abstractmethod

class PromptBuilderInterface(ABC):
    @abstractmethod
    def build_prompt(self,question:str,search_results:list[SearchResult])->str:
        pass
