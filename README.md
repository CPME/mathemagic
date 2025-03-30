# Mathemagic

An AI calculator agent that interprets and solves science, technology, mathematics, and engineering problems in Python.

## Basic Usage
```code
mathemagic

Mathemagic Calculator (Press Ctrl+C to exit)
Enter your math problem:
: Two hundred miles times 634 feet in meters squared.
Processing: Two hundred miles times 634 feet in meters squared.

Result:
62198956.89216 meter ** 2
```

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
uv run src/mathemagic/server.py
```

### Using the CLI

```bash
# Run the CLI with a math problem
uv run src/mathemagic/cli.py "100 miles times 234 acres in liters"

# Show the generated Python code along with the result
uv run src/mathemagic/cli.py "100 miles times 234 acres in liters" --output-python

# Or run in interactive mode
uv run src/mathemagic/cli.py
```

### Output the Executed Python Code
Using the -p or --output-python flags
````code
mathemagic -p

Mathemagic Calculator (Press Ctrl+C to exit)
Enter your math problem:
: Two hundred miles times 634 feet in meters squared.
Processing: Two hundred miles times 634 feet in meters squared.

Generated Python code:
```python
from pint import UnitRegistry

ureg = UnitRegistry()
Q_ = ureg.Quantity

# Define the variables with their respective units
miles = Q_(200, 'mile')  # distance in miles
feet = Q_(634, 'foot')  # distance in feet

# Perform the multiplication
result = miles * feet

# Convert the result to meters squared
result_m2 = result.to('meter**2')

print(result_m2)
```
Result:
62198956.89216 meter ** 2
````

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
