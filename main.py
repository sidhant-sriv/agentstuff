from dotenv import load_dotenv
from tools.mathematics import return_math_operations

load_dotenv()
from llama_index.core.agent import ReActAgent
from llama_index.llms.ollama import Ollama

llm = Ollama(model="llama3.1:8b-instruct-q8_0", request_timeout=120.0)
agent = ReActAgent.from_tools([*return_math_operations()], llm=llm, verbose=True)


response = agent.chat("What is (20*30)+(40/(3*22))? Calculate step by step.")

print(response)