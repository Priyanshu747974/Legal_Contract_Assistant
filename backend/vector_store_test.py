from app.infrastructure.chunks_embedders.sentence_embedding import SentenceTransformerEmbedding
from app.infrastructure.vectorDB_inserter.in_memory_vector_store import InMemoryVectorStore
from app.core.model.chunk import Chunk

# Sample chunks
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
    )
]

# Create embedder
embedder = SentenceTransformerEmbedding()

# Generate embeddings
embeddings = embedder.embed_chunks(chunks)

# Create vector store
vector_store = InMemoryVectorStore()

# Add embeddings
vector_store.add_embeddings(embeddings)

# Create a query
query = Chunk(
    chunk_id=0,
    text="How can I terminate the contract?",
    metadata={}
)

query_embedding = embedder.embed_chunks([query])[0]

# Search
results = vector_store.search(
    query_embedding.vector,
    k=2
)

# Print results
for result in results:
    print(f"Score: {result.score:.4f}")
    print(f"Chunk ID: {result.embedding.chunk.chunk_id}")
    print(f"Text: {result.embedding.chunk.text}")
    print("-" * 40)