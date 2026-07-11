from app.infrastructure.Parsed_chunkers.section_chunker import SectionChunker
from app.infrastructure.LLM.gemini_LLM import GeminiLLM
from app.infrastructure.parsers.pypdf_parser import PyPDFParser
from app.infrastructure.prompt_builder.prompt_builder_implementation import DefaultPromptBuilder
from app.infrastructure.retrieval.embedding_retriever import EmbeddingRetriever
from app.infrastructure.chunks_embedders.sentence_embedding import SentenceTransformerEmbedding
from app.infrastructure.vectorDB_inserter.in_memory_vector_store import InMemoryVectorStore 
from app.services.rag_services import RAGServices


parser = PyPDFParser()

chunker = SectionChunker()

embedder = SentenceTransformerEmbedding()

vector_store = InMemoryVectorStore()

retriever = EmbeddingRetriever(
    embedder,
    vector_store
)

prompt_builder = DefaultPromptBuilder()

llm = GeminiLLM()

rag_service = RAGServices(
    retriever,
    prompt_builder,
    llm
)

#document ingestion
print("Parsing PDF...")
document = parser.parse("documents/sample.pdf")
print("PDF parsed successfully!")

print("Chunking PDF...")
chunks = chunker.chunk(document)
print("PDF chunked successfully!")

print("Embedding chunks...")
embeddings = embedder.embed_chunks(chunks)
print("Chunks embedded successfully!")

print("Adding embeddings to vector store...")
vector_store.add_embeddings(embeddings) 
print("Embeddings added successfully!")

#question
print("Asking a question...")
question = input("Ask a question: ")

answer = rag_service.generate_answer(question)

print(answer)