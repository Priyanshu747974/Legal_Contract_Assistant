from app.core.model.parsed_document import ParsedDocument
from abc import ABC, abstractmethod

class PDFparserInterface:
    @abstractmethod
    def parse(self, pdf_path: str) -> ParsedDocument:
        pass
    
    
    