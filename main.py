
import os
import argparse
import json

from prompts import system_prompt 
from dotenv import load_dotenv
from openai import OpenAI
from call_function import available_functions, call_function

load_dotenv()

MAX_ITERATIONS = 20

parser = argparse.ArgumentParser(description="AI Agent")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument(
    "--verbose",
    action="store_true",
    help="Enable verbose output",
)
args = parser.parse_args()


api_key = os.environ.get("OPENROUTER_API_KEY")

if api_key is None:
    raise RuntimeError("OPENROUTER_API_KEY is not set")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

messages = [
    {
        "role": "system",
        "content": system_prompt,
    },
    {
        "role": "user",
        "content": args.user_prompt,
    },
]

for _ in range(MAX_ITERATIONS):
    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
        tools=available_functions,
        temperature=0,
    )

    message = response.choices[0].message

    messages.append(message)

    if not message.tool_calls:
       print("Final response:")
       print(message.content)
       break

    for tool_call in message.tool_calls:
        result_message = call_function(
            tool_call,
            verbose=args.verbose,
        )

        if not result_message["content"]:
            raise RuntimeError("Function call returned empty content")

        messages.append(result_message)

        if args.verbose:
            print(f"-> {result_message['content']}")

else:
    print("Error: Agent reached the maximum number of iterations")
