from abc import ABC, abstractmethod


class IngestionServiceInterface(ABC):

    @abstractmethod
    def ingest(self, pdf_path: str) -> int:
        """
        Ingest a PDF into the vector store.

        Returns:
            Number of chunks indexed.
        """
        pass