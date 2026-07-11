from app.infrastructure.Parsed_chunkers.section_chunker import SectionChunker
from app.infrastructure.LLM.gemini_LLM import GeminiLLM
from app.infrastructure.parsers.pypdf_parser import PyPDFParser
from app.infrastructure.prompt_builder.prompt_builder_implementation import DefaultPromptBuilder
from app.infrastructure.retrieval.embedding_retriever import EmbeddingRetriever
from app.infrastructure.chunks_embedders.sentence_embedding import SentenceTransformerEmbedding
from app.infrastructure.vectorDB_inserter.in_memory_vector_store import InMemoryVectorStore 
from app.services.rag_service import RAGServices
from app.services.ingestion_service import IngestionService

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

ingestion_service = IngestionService(
    parser,
    chunker,
    embedder,
    vector_store
)
