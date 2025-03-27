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
python -m src.mathemagic.client "100 miles times 234 acres in liters"

# Or run in interactive mode
python -m src.mathemagic.client
```

## Examples

- "Convert 100 kilometers per hour to miles per hour"
- "What is the volume of a cylinder with radius 5cm and height 10cm?"
- "If I have 3 apples and 4 oranges, how many pieces of fruit do I have?"
- "Calculate the kinetic energy of a 2kg object moving at 10 meters per second"

## Architecture

The application consists of:
- A server component that handles the conversion of natural language to Python code
- A client component that provides a command-line interface
- Integration with the Pint library for unit handling

See `mathemagic.mmd` for a visual representation of the architecture.
