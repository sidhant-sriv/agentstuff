from dotenv import load_dotenv
from llama_index.core.llms import llm
from tools.mathematics import return_math_operations
from tools.query import journal_tool
from tools.text_operations import return_text_operations

load_dotenv()
from llama_index.core.agent import ReActAgent
from llama_index.llms.ollama import Ollama
from llama_index.llms.gemini import Gemini

# llm = Ollama(model="llama3.1:8b-instruct-q8_0", request_timeout=120.0)
llm = Gemini()
agent = ReActAgent.from_tools(
    [*return_math_operations(), journal_tool, *return_text_operations()], llm=llm, verbose=True, max_iterations=12
)


response = agent.chat("Count all mentions of Chavz.")

print(response)
