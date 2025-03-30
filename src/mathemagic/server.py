import os
import asyncio
from typing import Dict, Any

from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv

from mathemagic import mathemagic

# Load environment variables
load_dotenv()

# Initialize MCP server
server = FastMCP("Mathemagic")

@server.tool()
async def handle_prompt_to_py(user_prompt: str) -> Dict[str, Any]:
    """
    Convert a user prompt to Python code.
    
    Args:
        user_prompt: The user's math problem or question
        
    Returns:
        A dictionary containing the Python code and status
    """
    try:
        python_code = mathemagic.prompt_to_py(user_prompt)
        return {
            "status": "success",
            "python_code": python_code,
            "extracted_code": mathemagic.extract_python_code(python_code)
        }
    except Exception as e:
        return {
            "status": "error",
            "error": str(e)
        }

@server.tool()
async def handle_execute_python(python_code: str) -> Dict[str, Any]:
    """
    Execute Python code and return the result.
    
    Args:
        python_code: The Python code to execute
        
    Returns:
        A dictionary containing the execution result and status
    """
    try:
        result, success = mathemagic.execute_py(python_code)
        return {
            "status": "success" if success else "error",
            "result": result
        }
    except Exception as e:
        return {
            "status": "error",
            "error": str(e)
        }

@server.tool()
async def handle_calculate(user_prompt: str) -> Dict[str, Any]:
    """
    Process a complete calculation: convert prompt to Python and execute it.
    
    Args:
        user_prompt: The user's math problem or question
        
    Returns:
        A dictionary containing the Python code, execution result, and status
    """
    try:
        # Convert prompt to Python
        python_code = mathemagic.prompt_to_py(user_prompt)
        extracted_code = mathemagic.extract_python_code(python_code)
        
        # Execute the Python code
        result, success = mathemagic.execute_py(python_code)
        
        return {
            "status": "success" if success else "error",
            "python_code": python_code,
            "extracted_code": extracted_code,
            "result": result
        }
    except Exception as e:
        return {
            "status": "error",
            "error": str(e)
        }

async def main():
    """Start the MCP server"""
    print("Starting Mathemagic MCP server...")
    
    # Handle graceful shutdown
    try:
        await server.run_sse_async()
    except KeyboardInterrupt:
        print("\nShutting down Mathemagic MCP server...")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nMCP server shutdown complete.")
