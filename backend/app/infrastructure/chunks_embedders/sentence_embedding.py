# pyrefly: ignore [missing-import]
from sentence_transformers import SentenceTransformer
from app.core.interfaces.transformer_embedding_interface import TransformerEmbeddingInterface
from app.core.model.chunk import Chunk
from app.core.model.embedding_model import EmbeddingModel

model = SentenceTransformer("all-MiniLM-L6-v2")

class SentenceTransformerEmbedding(TransformerEmbeddingInterface):
    def __init__(self):
        self.model=model
    def embed_chunks(self,chunks:list[Chunk])->list[EmbeddingModel]:
        texts = [chunk.text for chunk in chunks]
        vectors = self.model.encode(texts)

        embeddings=[]

        for chunk, vector in zip(chunks,vectors):
            embedding = EmbeddingModel(
                    chunk=chunk,  
                    vector=vector.tolist())
            embeddings.append(embedding)
            
        return embeddings

    def embed_query(self, query: str) -> list[float]:
        return self.model.encode(query).tolist()