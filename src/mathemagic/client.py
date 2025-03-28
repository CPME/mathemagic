#!/usr/bin/env python3
import asyncio
import sys
import argparse
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def process_problem(session, problem):
    """Process a math problem using the MCP server"""
    print(f"Processing: {problem}")
    
    # First, convert the problem to Python code
    python_code = await session.call_tool(
        "prompt_to_py",
        arguments={"user_prompt": problem}
    )
    
    print("\nGenerated Python code:")
    print("-" * 40)
    print(python_code)
    print("-" * 40)
    
    # Ask if the user wants to execute the code
    user_input = input("Execute this code? (y/n): ")
    if user_input.lower() in ["y", "yes"]:
        # Execute the Python code
        result = await session.call_tool(
            "execute_python",
            arguments={"python_code": python_code}
        )
        
        print("\nResult:")
        print("-" * 40)
        print(result)
        print("-" * 40)

async def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Mathemagic Calculator CLI")
    parser.add_argument("problem", nargs="*", help="Math problem to solve")
    args = parser.parse_args()
    
    # Create server parameters for connecting to the MCP server
    server_params = StdioServerParameters(
        command="python",
        args=["-m", "mathemagic.server"],
    )
    
    try:
        async with stdio_client(server_params) as (read, write):
            async with ClientSession(read, write) as session:
                # Initialize the connection
                await session.initialize()
                print("Connected to Mathemagic Calculator successfully")
                
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
                            await process_problem(session, user_input)
                            
                        except KeyboardInterrupt:
                            print("\nExiting...")
                            break
                        except Exception as e:
                            print(f"Error: {str(e)}")
                else:
                    # Process the problem provided as command-line arguments
                    problem = " ".join(args.problem)
                    await process_problem(session, problem)
    
    except KeyboardInterrupt:
        print("\nExiting gracefully...")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(main())
