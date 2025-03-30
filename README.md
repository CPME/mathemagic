# Mathemagic
An AI calculator agent that interprets and solves science, technology, mathematics, and engineering problems in Python.

- [Source Code](https://github.com/CPME/mathemagic)
- [pypi](https://pypi.org/project/mathemagic-ai/)

<img src="./resources/mathemagic.png" alt="Mathemagic" width="420"/>

## Features
- Converts natural language math problems to Python code using LLMs (Claude is currently the only supported model)
- Handles units using the [Pint](https://github.com/hgrecco/pint/tree/master) library
- Provides access through MCP and CLI interfaces
- Supports complex mathematical operations with proper unit handling

## Example Inputs
- "Convert 100 kilometers per hour to miles per hour"
- "What is the volume of a cylinder with radius 5cm and height 10cm?"
- "If I have 3 apples and 4 oranges, how many pieces of fruit do I have?"
- "Calculate the kinetic energy of a 2kg object moving at 10 meters per second"

## Basic Usage
Enter command to start CLI
```bash
mathemagic
```
CLI initializes, and you type in your math problem
```code
Mathemagic Calculator (Press Ctrl+C to exit)
Enter your math problem:
: Two hundred miles times 634 feet in meters squared.
Processing: Two hundred miles times 634 feet in meters squared.

Result:
62198956.89216 meter ** 2
```

## Quickstart
### Installing Mathemagic
If you already installed uv, activated a virtual environment, and created a `.env` file with your Anthropic API key installation is simple:
```bash
uv add mathemagic-ai
``` 
If not, please see "Detailed Setup" for more info.

## Detailed Setup
### Creating an Anthropic Account
You'll also need an anthropic API key. This requires you set up a developer console, and add payment information. Running commands costs pennies.

To set up an account and get an API key:
1. Set up an account for the [Anthropic Console](https://console.anthropic.com/login?returnTo=%2F%3F)
1. Add billing details
1. Buy credits (you can use the minumum)
1. Create an API key

*I may add support for other model providers in the future

### Setting up API key as an Environment Variable
Create a `.env` file with your Anthropic API key in your project root directory. 

If you already have a `.env` file, this command adds the api key.
```bash
echo "ANTHROPIC_API_KEY=your_api_key_here" >> .env
```

### Installing uv & Setting Up a Virtual Environment
You can use pip if you prefer, but I highly recommend uv.

If you need to install uv, this is the basic command to install it on macOS and Linux. If it doesn't work, troubleshoot with instructions listed at [installing uv](https://docs.astral.sh/uv/getting-started/installation/#pypi).

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

I also higly recommend setting up a virtual environment.
```bash
# Create a virtual environment
uv venv
# Activate the virtual environment
source .venv/bin/activate
# Initialize the project with a pyproject.toml
uv init
```

## Installation from Source (more advanced)
This is currently the only supported method for using the MCP server.

```bash
# Clone the repository
git clone https://github.com/yourusername/mathemagic.git
cd mathemagic

# Install dependencies using UV
uv pip install -e .

```
## Detailed CLI Usage
### Example Usages
```bash
# Run in interactive mode
mathemagic

# Run the CLI with a math problem
mathemagic "100 miles times 234 acres in liters"

# Show the generated Python code along with the result
mathemagic "100 miles times 234 acres in liters" --output-python

# help menu
mathemagic --help
```

### Output the Executed Python Code
Using the -p or --output-python flags
```bash
mathemagic -p
```
````code
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

#### Handles Arbitrary Units
mathemagic uses Pint to handle units.
```code
Enter another problem:
: 100 bananas times 66 guavas
Processing: 100 bananas times 66 guavas

Result:
6600 banana * guava
```
### Using the MCP Server
#### Starting the Server
```bash
# Start the MCP server
uv run src/mathemagic/server.py
```
### Add the MCP Server to Claude Code
Assuming you have claude code installed, type this command, then follow the wizard. You'll enter the command above when prompted.
```bash
claude mcp add
```

## Architecture
The application consists of:
- `mathemagic.py`: Core functionality for converting natural language to Python code and executing it
- `server.py`: MCP server that provides API endpoints for the calculator
- `cli.py`: Command-line interface for interacting with the calculator

# TODO
1. Support for running MCP server with mathemagic installed as a package from pypi
1. Clean up python output through server (currently outputs in a dict and not pretty)
1. Improve CLI (make it pretty)
1. Update spec.md?
1. Add symbolic math support
1. Add linear algebra support
1. Update to use openrouter
1. Add tests
1. Astropy support?
1. Auth as alternative to .env for remote use?