from dotenv import load_dotenv
from llama_index.core.llms import llm
from hardware import return_serial_hardware_operations
from tools.mathematics import math_operations, return_math_operations
# from tools.query import journal_tool
from tools.text_operations import return_text_operations

load_dotenv()
from llama_index.core.agent import ReActAgent
from llama_index.llms.ollama import Ollama
from llama_index.llms.gemini import Gemini

llm = Ollama(model="llama3.1:8b-instruct-q8_0", request_timeout=120.0)
# llm = Gemini()
agent = ReActAgent.from_tools(
    [*return_serial_hardware_operations()], llm=llm, verbose=True, max_iterations=10
)

agent.get_prompts()
print("running")
# Example commands:
# response = agent.chat("Turn on the LED")
# response = agent.chat("Move the servo to 90 degrees")
response = agent.chat("If object is more than 10cm away then turn off the led")
# response = agent.chat("Turn the servo to 45 degrees and then turn on the LED")

print(response)