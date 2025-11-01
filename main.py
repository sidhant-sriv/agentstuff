from dotenv import load_dotenv
from llama_index.core.llms import llm
from hardware import return_serial_hardware_operations
from tools.mathematics import math_operations, return_math_operations
# from tools.query import journal_tool
from tools.text_operations import return_text_operations
import os
import asyncio

load_dotenv()
from llama_index.core.agent import FunctionAgent
from llama_index.llms.ollama import Ollama
from llama_index.llms.gemini import Gemini
from llama_index.llms.groq import Groq

# Choose your LLM provider (uncomment the one you want to use)
# llm = Ollama(model="qwen2.5:14b", request_timeout=120.0)
# llm = Gemini()
llm = Groq(model="openai/gpt-oss-120b", api_key=os.getenv("GROQ_API_KEY"))
# llm = Groq(model="llama-3.3-70b-versatile", api_key=os.getenv("GROQ_API_KEY"))
# llm = Groq(model="mixtral-8x7b-32768", api_key=os.getenv("GROQ_API_KEY"))

# Create agent with FunctionAgent for better tool calling and reasoning visibility
agent = FunctionAgent(
    tools=return_serial_hardware_operations(), 
    llm=llm, 
    verbose=True
)

async def main():
    """Main async function to run the agent loop"""
    print("=" * 60)
    print("Hardware Control Agent Ready!")
    print("=" * 60)
    print("\nAvailable commands:")
    print("  - Control servo: 'Move servo to 90 degrees'")
    print("  - Control LED: 'Turn on the LED' / 'Turn off the LED'")
    print("  - Measure distance: 'How far is the object?'")
    print("  - Complex tasks: 'If object is less than 10cm, turn on LED'")
    print("\nType 'exit' or 'quit' to stop the agent.\n")
    print("=" * 60)

    # Continuous input loop
    while True:
        try:
            user_input = input("\nYou: ").strip()
            
            if not user_input:
                continue
                
            if user_input.lower() in ['exit', 'quit', 'q']:
                print("\nClosing hardware connection and exiting...")
                from hardware import close_serial_connection
                close_serial_connection()
                print("Goodbye!")
                break
            
            print("\nAgent: Processing your request...\n")
            print("=" * 60)
            # Run the async agent method
            response = await agent.run(user_input)
            print("=" * 60)
            print(f"\nFinal Response: {response}\n")
            print("-" * 60)
            
        except KeyboardInterrupt:
            print("\n\nInterrupted by user. Closing connection...")
            from hardware import close_serial_connection
            close_serial_connection()
            print("Goodbye!")
            break
        except Exception as e:
            print(f"\nError occurred: {e}")
            import traceback
            traceback.print_exc()
            print("Continuing... (type 'exit' to quit)\n")

if __name__ == "__main__":
    asyncio.run(main())
