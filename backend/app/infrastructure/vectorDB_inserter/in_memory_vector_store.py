from app.core.interfaces.vectorstore import VectorStoreInterface
from app.core.model.embedding_model import EmbeddingModel
from app.core.model.search_result_vDB import SearchResult

class InMemoryVectorStore(VectorStoreInterface):
    def __init__(self):
        self._embeddings: list[EmbeddingModel]=[]

    def add_embeddings(self, embeddings: list[EmbeddingModel]) -> None:
        self._embeddings.extend(embeddings)

    def search(self, query_vector: list[float], k: int) -> list[SearchResult]:
        results: list[SearchResult] = []
        for embedding in self._embeddings:
            score = self._cosine_similarity(query_vector, embedding.vector)
            results.append(SearchResult(embedding=embedding, score=score))
        results.sort(key=lambda result: result.score, reverse=True)
        return results[:k]

    def _cosine_similarity(self, vec1: list[float], vec2: list[float]) -> float:
        dot_product = sum(a * b for a, b in zip(vec1, vec2))
        norm_a = sum(a * a for a in vec1) ** 0.5
        norm_b = sum(b * b for b in vec2) ** 0.5
        if norm_a == 0 or norm_b == 0:
            return 0
        return dot_product / (norm_a * norm_b)
