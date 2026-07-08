from app.infrastructure.chunks_embedders.sentence_embedding import (
    SentenceTransformerEmbedding,
)
from app.infrastructure.vectorDB_inserter.in_memory_vector_store import (
    InMemoryVectorStore,
)
from app.infrastructure.retrieval.embedding_retriever import (
    EmbeddingRetriever,
)

from app.core.model.chunk import Chunk

# Create sample chunks
chunks = [
    Chunk(
        chunk_id=1,
        text="The agreement may be terminated by either party.",
        metadata={}
    ),
    Chunk(
        chunk_id=2,
        text="Payment shall be made within 30 days.",
        metadata={}
    ),
    Chunk(
        chunk_id=3,
        text="This contract is governed by Indian law.",
        metadata={}
    ),
]

# Create embedder
embedder = SentenceTransformerEmbedding()

# Generate embeddings
embeddings = embedder.embed_chunks(chunks)

# Create vector store
vector_store = InMemoryVectorStore()
vector_store.add_embeddings(embeddings)

# Create retriever
retriever = EmbeddingRetriever(
    embedder=embedder,
    vector_store=vector_store
)

# Retrieve
results = retriever.retrieve(
    query="How can I terminate the contract?",
    k=2
)

# Print results
for result in results:
    print(f"Score: {result.score:.4f}")
    print(result.embedding.chunk.text)
    print("-" * 40)