# Mathemagic

An AI calculator agent that interprets and solves science, technology, mathematics, and engineering problems in Python.

## Features

- Converts natural language math problems to Python code
- Handles units using the Pint library
- Provides access through MCP and CLI interfaces
- Supports complex mathematical operations with proper unit handling

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/mathemagic.git
cd mathemagic

# Install dependencies using UV
uv pip install -e .

# Set up environment variables
# Create a .env file with your Anthropic API key:
# ANTHROPIC_API_KEY=your_api_key_here
```

## Usage

### Starting the Server

```bash
# Start the MCP server
python -m src.mathemagic.server
```

### Using the CLI

```bash
# Run the CLI with a math problem
python -m src.mathemagic.cli "100 miles times 234 acres in liters"

# Show the generated Python code along with the result
python -m src.mathemagic.cli "100 miles times 234 acres in liters" --output-python

# Or run in interactive mode
python -m src.mathemagic.cli
```

### Generating UML Diagram

```bash
# Generate a UML diagram of the codebase
python -m src.mathemagic.code_to_uml
```

## Examples

- "Convert 100 kilometers per hour to miles per hour"
- "What is the volume of a cylinder with radius 5cm and height 10cm?"
- "If I have 3 apples and 4 oranges, how many pieces of fruit do I have?"
- "Calculate the kinetic energy of a 2kg object moving at 10 meters per second"

## Architecture

The application consists of:
- `mathemagic.py`: Core functionality for converting natural language to Python code and executing it
- `server.py`: MCP server that provides API endpoints for the calculator
- `cli.py`: Command-line interface for interacting with the calculator
- `code_to_uml.py`: Utility for generating UML diagrams of the codebase

See `mathemagic.mmd` for a visual representation of the architecture.
