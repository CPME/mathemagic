import pint
import re

# Initialize the unit registry
ureg = pint.UnitRegistry()
Q_ = ureg.Quantity

def convert_prompt_to_python(system_prompt, user_prompt):
    """
    Combines system prompt and user prompt to prepare for LLM processing.
    
    Args:
        system_prompt (str): The system instructions
        user_prompt (str): The user's math problem
        
    Returns:
        str: Combined prompt for LLM
    """
    return f"{system_prompt}\n\nUser Prompt:\n\"{user_prompt}\""

def execute_python(python_code):
    """
    Executes the Python code generated from the user prompt.
    
    Args:
        python_code (str): Python code to execute
        
    Returns:
        str: Result of the execution
    """
    # Create a local namespace with the necessary imports
    local_namespace = {
        'ureg': ureg,
        'Q_': Q_,
        'pint': pint
    }
    
    # Remove the markdown code block markers if present
    python_code = re.sub(r'^```python\s*', '', python_code)
    python_code = re.sub(r'\s*```$', '', python_code)
    
    try:
        # Capture stdout to get the printed results
        import io
        import sys
        original_stdout = sys.stdout
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        # Execute the code
        exec(python_code, local_namespace)
        
        # Restore stdout and get the captured output
        sys.stdout = original_stdout
        result = captured_output.getvalue()
        
        return result if result else "Code executed successfully but produced no output."
    
    except Exception as e:
        return f"Error executing code: {str(e)}"
