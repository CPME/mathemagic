# Specification Template
> Ingest the information from this file, implement the Low-Level Tasks, and generate the code that will satisfy the High and Mid-Level Objectives.

## High-Level Objective

- Build a ai calculator agent to interperet and solve science, technology, mathematics, and engineering problems in python

## Mid-Level Objective

- Convert a user prompt containing a math problem to python
- Handle units using Pint python library
- Provide access to functions through MCP and CLI interfaces

## Implementation Notes
- Use only the dependencies in pyproject.toml (don't use anything else)
- Use the provided system prompt system_instruction.md
- The client can be used as a command line interface to test the server
- Use UV, don't use pip or python commands
- Update README.md as you go.
- Ability to use 'ctrl + c' to interrupt processes gracefully
- Client connects to anthropic API

## Context
 - spec.md

### Beginning context
- spec.md
- pyproject.toml
- src/mathemagic/system_instruction.md

### Ending context  
- spec.md
- pyproject.toml
- src/mathemagic/mathemagic.py (NEW)
- src/mathemagic/server.py (NEW)
- src/mathemagic/cli.py (NEW)
- src/mathemagic/code_to_uml.py (NEW)
- mathemagic.mmd (new)

## Low-Level Tasks
> Ordered from start to finish

1. [First task - Create the basic functionality of the agent in mathemagic.py]
```aider
CREATE src/mathemagic/mathemagic.py
system_prompt = src/mathemagic/system_instruction.md (import content from this file as a string)
prompt_to_py(system_prompt, user_prompt) 
py_prompt = (system_prompt + user_prompt)
    pass py_prompt to llm using anthropic api.
    receive math_as_py
    return response to prompt (which will be python)
execute_py(response)
    Exract python from response
    Execute python
    return result

2. [Second task - Create a basic command line interface in a new file that also acts as a lightweight command line tool to interact with the server.]
```aider
Create src/mathemagic/cli.py using the typer library.
    initialize the server
    Prompt user for input
    Pass input to server
    display response to the user
    Prompt the user for another input.
    handle "ctrl + c" keyboard interrupt gracefully
Add an initialization flag --output-python to return math_as_py to the user as well as result.
Create a help menu, accessible with the -h or --help flag.
```

3. [Second task - Create an MCP server in a new file referencing the core functions from mathemagic.py]
```aider
CREATE src/mathemagic/server.py
call prompt_to_py(user_prompt) 
    get user prompt from client
call mathemagic.prompt_to_py(system_prompt, user_prompt)
...wait for llm to return math as python
execute_python(user_prompt) ## runs when client returns python code (client selects "execute_python")
```
4. [ - Write a test to validate the server functionality]
Create test_server.py
    mock the client behavior by passing the user prompt to the server.
    test the MCP server connection

5. [Third task - create a mermaid diagram to show how the application works]
```aider
Create src/mathemagic/code_to_uml.py to generate uml.mmd a uml class diagram in mermaid format from the codebase using pyreverse from the pylint library.
```