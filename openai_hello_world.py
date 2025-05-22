"""
OpenAI Hello World Program

This script demonstrates how to use the OpenAI API to generate a simple "Hello World" response
from a large language model (LLM). It authenticates with the API, sends a prompt to the LLM,
and prints the generated response.

Requirements:
- OpenAI Python package (install with: pip install openai)
- An OpenAI API key (set as an environment variable OPENAI_API_KEY)

Usage:
- Set your OpenAI API key as an environment variable OPENAI_API_KEY
- Run the script: python openai_hello_world.py
"""
import os  # For accessing environment variables
import openai  # For interacting with the OpenAI API

# Authentication setup
# The API key is needed to authenticate with OpenAI's services
# We get it from environment variables for security best practices
api_key = os.getenv("OPENAI_API_KEY")  # Retrieve API key from environment variable
if not api_key:
    # If the API key is not found, raise an error with instructions
    raise ValueError("Please set the OPENAI_API_KEY environment variable.")

# Initialize the OpenAI client with the API key
client = openai.OpenAI(api_key=api_key)

# Define the model we want to use and the prompt
model = "gpt-3.5-turbo"  # Using GPT-3.5 Turbo for good performance at reasonable cost
prompt = "Say Hello World"  # The instruction to give to the LLM

# Call the OpenAI API to generate a response
# Using the chat completions endpoint which is designed for conversational interactions
response = client.chat.completions.create(
    model=model,
    messages=[
        {"role": "user", "content": prompt}  # The role is "user" to simulate a user query
    ]
)

# Extract and print the generated response
# The API returns a structured response with multiple fields; we only need the message content
print("LLM Response:")
print(response.choices[0].message.content)
