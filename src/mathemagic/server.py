import os
import sys
import traceback
from pathlib import Path
from mcp.server.fastmcp import FastMCP, Context
from pint import UnitRegistry

# Create a unit registry for handling units
ureg = UnitRegistry()

# Create an MCP server
mcp = FastMCP("Mathemagic Calculator")

# Load the system instruction
def load_system_instruction():
    """Load the system instruction from the system_instruction.md file."""
    current_dir = Path(__file__).parent
    system_instruction_path = current_dir / "system_instruction.md"
    
    with open(system_instruction_path, "r") as f:
        return f.read()

system_prompt = load_system_instruction()

@mcp.tool()
def prompt_to_py(user_prompt: str, ctx: Context) -> str:
    """
    Convert a user's math problem to executable Python code.
    
    Args:
        user_prompt: The user's math problem or question
        ctx: The MCP context
        
    Returns:
        Python code that solves the math problem
    """
    ctx.info(f"Converting user prompt to Python: {user_prompt}")
    
    # Use the sampling mechanism to convert the math problem to Python
    full_prompt = f"{system_prompt}\n\nUser Problem: {user_prompt}\n\nPython Solution:"
    return full_prompt

@mcp.tool()
def execute_python(python_code: str, ctx: Context) -> str:
    """
    Execute the Python code generated from the user's math problem.
    
    Args:
        python_code: The Python code to execute
        ctx: The MCP context
        
    Returns:
        The result of executing the Python code
    """
    ctx.info(f"Executing Python code: {python_code}")
    
    try:
        # Create a local namespace with necessary imports and the unit registry
        local_namespace = {
            "ureg": ureg,
            "Q_": ureg.Quantity,
            "__builtins__": __builtins__,
        }
        
        # Execute the code in the local namespace
        exec("import math, numpy as np", local_namespace)
        exec(python_code, local_namespace)
        
        # Look for a result variable or the last expression
        if "result" in local_namespace:
            return str(local_namespace["result"])
        else:
            # If no result variable, return a generic success message
            return "Code executed successfully, but no explicit result was returned."
    
    except Exception as e:
        error_msg = f"Error executing Python code: {str(e)}\n{traceback.format_exc()}"
        ctx.error(error_msg)
        return error_msg

if __name__ == "__main__":
    mcp.run()
