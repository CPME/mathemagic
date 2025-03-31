import sys
import typer
from typing import Optional
import signal
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich.text import Text

try:
    # Try relative import first (for when used as a package)
    from . import mathemagic
except ImportError:
    # Fall back to absolute import (for when run directly)
    import sys
    from pathlib import Path
    # Add the src directory to the path
    sys.path.insert(0, str(Path(__file__).parent.parent))
    # Import the module directly
    from mathemagic import mathemagic

# Create a Typer app for compatibility with entry points
app = typer.Typer(help="Mathemagic: AI calculator for science and engineering problems")

# Create a Rich console for pretty output
console = Console()


@app.command()
def main(
    problem: Optional[str] = typer.Argument(None, help="Math problem to solve"),
    output_python: bool = typer.Option(False, "--output-python", "-p", help="Output the generated Python code")
):
    """
    Convert a natural language math problem to Python and execute it.
    
    If no problem is provided, enters interactive mode.
    """
    # Handle Ctrl+C gracefully
    def signal_handler(sig, frame):
        # Print a newline to avoid showing ^C
        print("", end="\r")
        console.print("[italic]Exiting Mathemagic. Goodbye![/italic]")
        sys.exit(0)
        
    signal.signal(signal.SIGINT, signal_handler)
    
    if problem:
        process_problem(problem, output_python)
    else:
        # Interactive mode
        title = Text("✨ Mathemagic Calculator ✨", style="bold blue")
        content = Text("AI-powered calculator for science and engineering problems\nPress Ctrl+C to exit", style="italic")
        panel = Panel(content, title=title, border_style="blue", padding=(1, 2))
        console.print(panel)
        console.print("Enter your math problem -")
        
        while True:
            try:
                problem = typer.prompt("")
                process_problem(problem, output_python)
                console.print("\nEnter another problem -")
            except KeyboardInterrupt:
                # Print a newline to avoid showing ^C
                print("", end="\r")
                console.print("[italic]Exiting Mathemagic. Goodbye![/italic]")
                sys.exit(0)


def process_problem(problem: str, output_python: bool):
    """Process a single math problem"""
    console.print(f"[bold]Processing:[/bold] {problem}")
    
    # Convert problem to Python
    python_code = mathemagic.prompt_to_py(problem)
    
    # Show Python code if requested
    if output_python:
        console.print("\n[bold]Generated Python code:[/bold]")
        code_block = f"```python\n{mathemagic.extract_python_code(python_code)}\n```"
        console.print(Markdown(code_block))
    
    # Execute the Python code
    result, success = mathemagic.execute_py(python_code)
    
    # Display result
    console.print("\n[bold]Result:[/bold]")
    if success:
        # Try to render the result as markdown
        console.print(Markdown(str(result)))
    else:
        console.print(f"[bold red]Error:[/bold red] {result}")


if __name__ == "__main__":
    app()
