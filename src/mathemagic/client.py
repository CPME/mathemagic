import asyncio
import argparse
import sys
from mcp import Client

async def main():
    """
    Main function to run the client CLI.
    """
    parser = argparse.ArgumentParser(description="Mathemagic CLI - AI Calculator for STEM problems")
    parser.add_argument("--prompt", type=str, help="Math problem to solve")
    parser.add_argument("--execute", type=str, help="Execute Python code directly")
    
    args = parser.parse_args()
    
    client = Client()
    
    if args.prompt:
        # First, convert the prompt
        print("Converting prompt to Python code...")
        response = await client.call_function("convert_prompt", args.prompt)
        print("\nSend this to an LLM:")
        print(response)
        
        # Ask user if they want to execute the code
        python_code = input("\nPaste the Python code from the LLM response to execute (or press Enter to skip): ")
        if python_code.strip():
            result = await client.call_function("execute_python", python_code)
            print("\nExecution result:")
            print(result)
    
    elif args.execute:
        # Execute Python code directly
        result = await client.call_function("execute_python", args.execute)
        print("\nExecution result:")
        print(result)
    
    else:
        # Interactive mode
        print("Mathemagic CLI - AI Calculator for STEM problems")
        print("Enter a math problem or type 'exit' to quit")
        
        while True:
            user_input = input("\nMath problem: ")
            if user_input.lower() in ["exit", "quit"]:
                break
            
            # Convert the prompt
            response = await client.call_function("convert_prompt", user_input)
            print("\nSend this to an LLM:")
            print(response)
            
            # Ask user for the LLM response
            python_code = input("\nPaste the Python code from the LLM response (or press Enter to skip): ")
            if python_code.strip():
                result = await client.call_function("execute_python", python_code)
                print("\nExecution result:")
                print(result)

if __name__ == "__main__":
    asyncio.run(main())
