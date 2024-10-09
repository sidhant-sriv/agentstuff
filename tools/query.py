from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, Settings
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.core.tools import QueryEngineTool
from llama_index.llms.gemini import Gemini
from llama_index.embeddings.gemini import GeminiEmbedding

from dotenv import load_dotenv
load_dotenv()
# Settings.llm = Gemini()

# Settings.embed_model = GeminiEmbedding(
#     model_name="models/embedding-001",
# )

Settings.llm = Ollama(model="llama3.1:8b-instruct-q8_0", request_timeout=120.0)
Settings.embed_model = OllamaEmbedding(
    model_name="nomic-embed-text:latest", request_timeout=120.0
)
documents = SimpleDirectoryReader("data/thoughts").load_data()
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()

journal_tool = QueryEngineTool.from_defaults(
    query_engine,
    name="Journal tool",
    description="A RAG Engine for text content.",
)
