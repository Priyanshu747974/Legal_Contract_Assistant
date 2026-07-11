from app.core.interfaces.ingestion_service_interface import (
    IngestionServiceInterface,
)
from app.core.interfaces.pdf_parser import PDFparserInterface
from app.core.interfaces.chunker import ChunkerInterface
from app.core.interfaces.transformer_embedding_interface import TransformerEmbeddingInterface
from app.core.interfaces.vectorstore import VectorStoreInterface


class IngestionService(IngestionServiceInterface):

    def __init__(
        self,
        parser: PDFparserInterface,
        chunker: ChunkerInterface,
        embedder: TransformerEmbeddingInterface,
        vector_store: VectorStoreInterface,
    ):
        self.parser = parser
        self.chunker = chunker
        self.embedder = embedder
        self.vector_store = vector_store

    def ingest(self, pdf_path: str) -> int:

        document = self.parser.parse(pdf_path)

        chunks = self.chunker.chunk(document)

        embeddings = self.embedder.embed_chunks(chunks)

        self.vector_store.add_embeddings(embeddings)

        return len(chunks)
