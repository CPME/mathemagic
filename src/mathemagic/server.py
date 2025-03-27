import os
import sys
from io import StringIO
from pathlib import Path
from mcp.server.fastmcp import FastMCP, Context
from dotenv import load_dotenv
import pint

# Load environment variables
load_dotenv()

# Create a unit registry for handling units
ureg = pint.UnitRegistry()
Q_ = ureg.Quantity

# Read the system instruction
current_dir = Path(__file__).parent
system_instruction_path = current_dir / "system_instruction.md"
with open(system_instruction_path, "r") as f:
    system_prompt = f.read()

# Create an MCP server
mcp = FastMCP("Mathemagic Calculator")

@mcp.tool()
async def prompt_to_py(user_prompt: str, ctx: Context) -> str:
    """
    Convert a user prompt containing a math problem to Python code.
    
    Args:
        user_prompt: The user's math problem
        ctx: The MCP context
        
    Returns:
        Python code that solves the math problem
    """
    ctx.info(f"Converting user prompt to Python: {user_prompt}")
    
    # Combine system prompt and user prompt
    full_prompt = f"{system_prompt}\n\nUser Prompt:\n{user_prompt}"
    
    # This will be handled by the LLM through MCP's sampling mechanism
    return full_prompt

@mcp.tool()
async def execute_python(python_code: str, ctx: Context) -> str:
    """
    Execute the Python code generated from the user prompt.
    
    Args:
        python_code: The Python code to execute
        ctx: The MCP context
        
    Returns:
        The result of executing the Python code
    """
    ctx.info("Executing Python code")
    
    # Remove markdown code block formatting if present
    if python_code.startswith("```python"):
        python_code = python_code.replace("```python", "", 1)
        if python_code.endswith("```"):
            python_code = python_code[:-3]
    
    # Create a local namespace with Pint objects
    local_namespace = {
        "ureg": ureg,
        "Q_": Q_,
        "pint": pint
    }
    
    # Capture stdout to return the result
    original_stdout = sys.stdout
    sys.stdout = output_capture = StringIO()
    
    try:
        # Execute the code in the local namespace
        exec(python_code, local_namespace)
        result = output_capture.getvalue()
        return result if result else "Code executed successfully but produced no output."
    except Exception as e:
        return f"Error executing code: {str(e)}"
    finally:
        sys.stdout = original_stdout

if __name__ == "__main__":
    mcp.run()
