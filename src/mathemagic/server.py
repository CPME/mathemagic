import os
import asyncio
from mcp import Server
from dotenv import load_dotenv
from mathemagic.mathemagic import convert_prompt_to_python, execute_python

# Load environment variables
load_dotenv()

# Read system instruction
with open(os.path.join(os.path.dirname(__file__), "system_instruction.md"), "r") as f:
    SYSTEM_INSTRUCTION = f.read()

async def handle_convert_prompt(user_prompt):
    """
    MCP handler for converting a user prompt to Python code.
    
    Args:
        user_prompt (str): The user's math problem
        
    Returns:
        str: The combined prompt for LLM processing
    """
    return convert_prompt_to_python(SYSTEM_INSTRUCTION, user_prompt)

async def handle_execute_python(python_code):
    """
    MCP handler for executing Python code.
    
    Args:
        python_code (str): Python code to execute
        
    Returns:
        str: Result of the execution
    """
    return execute_python(python_code)

async def main():
    """
    Main function to start the MCP server.
    """
    server = Server()
    
    # Register the functions
    server.register_function(
        "convert_prompt",
        handle_convert_prompt,
        description="Convert a math problem to a prompt for LLM processing"
    )
    
    server.register_function(
        "execute_python",
        handle_execute_python,
        description="Execute Python code generated from a math problem"
    )
    
    # Start the server
    await server.start()

if __name__ == "__main__":
    asyncio.run(main())
