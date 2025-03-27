#!/usr/bin/env python3
import asyncio
import argparse
import sys
from mcp.client.fastmcp import Client

async def main():
    parser = argparse.ArgumentParser(description="Mathemagic Calculator CLI")
    parser.add_argument("problem", nargs="*", help="Math problem to solve")
    parser.add_argument("--server", default="http://localhost:8000", help="MCP server URL")
    args = parser.parse_args()

    # Connect to the MCP server
    client = Client(args.server)
    
    # If no arguments provided, enter interactive mode
    if not args.problem:
        print("Mathemagic Calculator CLI")
        print("Type 'exit' or 'quit' to exit")
        print("Enter your math problem:")
        
        while True:
            try:
                user_input = input("> ")
                if user_input.lower() in ["exit", "quit"]:
                    break
                
                await process_problem(client, user_input)
            except KeyboardInterrupt:
                print("\nExiting...")
                break
            except Exception as e:
                print(f"Error: {e}")
    else:
        # Process the problem provided as command line arguments
        problem = " ".join(args.problem)
        await process_problem(client, problem)

async def process_problem(client, problem):
    print(f"Processing: {problem}")
    
    # First, convert the problem to Python code
    python_code = await client.call("prompt_to_py", problem)
    
    # Display the generated Python code
    print("\nGenerated Python code:")
    print(python_code)
    
    # Ask if the user wants to execute the code
    user_choice = input("\nExecute this code? (y/n): ")
    if user_choice.lower() == 'y':
        # Execute the Python code
        result = await client.call("execute_python", python_code)
        print("\nResult:")
        print(result)

if __name__ == "__main__":
    asyncio.run(main())
