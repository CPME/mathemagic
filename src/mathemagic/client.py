#!/usr/bin/env python3
import asyncio
import argparse
import sys
from mcp.client import Client

async def main():
    parser = argparse.ArgumentParser(description="Mathemagic Calculator CLI")
    parser.add_argument("problem", nargs="*", help="Math problem to solve")
    parser.add_argument("--server", default="http://localhost:8000", help="MCP server URL")
    args = parser.parse_args()

    # Connect to the MCP server
    client = Client(args.server)
    
    # If no problem is provided, enter interactive mode
    if not args.problem:
        print("Mathemagic Calculator CLI")
        print("Type 'exit' or 'quit' to exit")
        print("Enter your math problem:")
        
        while True:
            try:
                user_input = input("> ")
                if user_input.lower() in ["exit", "quit"]:
                    break
                
                if not user_input.strip():
                    continue
                
                # Process the problem
                await process_problem(client, user_input)
                
            except KeyboardInterrupt:
                print("\nExiting...")
                break
            except Exception as e:
                print(f"Error: {str(e)}")
    else:
        # Process the problem provided as command-line arguments
        problem = " ".join(args.problem)
        await process_problem(client, problem)

async def process_problem(client, problem):
    print(f"Processing: {problem}")
    
    # First, convert the problem to Python code
    python_code = await client.prompt_to_py(problem)
    print("\nGenerated Python code:")
    print("-" * 40)
    print(python_code)
    print("-" * 40)
    
    # Ask if the user wants to execute the code
    user_input = input("Execute this code? (y/n): ")
    if user_input.lower() in ["y", "yes"]:
        # Execute the Python code
        result = await client.execute_python(python_code)
        print("\nResult:")
        print("-" * 40)
        print(result)
        print("-" * 40)

if __name__ == "__main__":
    asyncio.run(main())
