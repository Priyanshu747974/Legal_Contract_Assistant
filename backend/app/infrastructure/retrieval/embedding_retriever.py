from app.core.interfaces.retriever import RetrieverInterface
from app.core.interfaces.transformer_embedding_interface import (
    TransformerEmbeddingInterface,
)
from app.core.interfaces.vectorstore import VectorStoreInterface
from app.core.model.search_result_vDB import SearchResult

class EmbeddingRetriever(RetrieverInterface):
    def __init__(self, embedder:TransformerEmbeddingInterface,
                    vector_store:VectorStoreInterface):
        self.embedder = embedder
        self.vector_store = vector_store

    def retrieve(self, query:str,k:int)->list[SearchResult]:
        query_vector = self.embedder.embed_query(query)

        results = self.vector_store.search(
            query_vector=query_vector,
            k=k,
        )
        return results