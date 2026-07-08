from app.core.model.parsed_document import ParsedDocument
from app.core.model.chunk import Chunk
from abc import ABC,abstractmethod

class ChunkerInterface(ABC):
    @abstractmethod
    def chunk(self, document: ParsedDocument)->list[Chunk]:
        pass
    