
import os
from pathlib import Path
import time
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Locate the main project directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Load environment variables
load_dotenv(BASE_DIR / ".env")

# Read Gemini configuration
api_key = os.getenv("GEMINI_API_KEY")
model_name = os.getenv("GEMINI_MODEL")

# Validate configuration
if not api_key:
    raise ValueError("GEMINI_API_KEY is missing!")

if not model_name:
    raise ValueError("GEMINI_MODEL is missing!")

# Initialize Gemini client
client = genai.Client(
    api_key=api_key,
    http_options=types.HttpOptions(
        timeout=30000,
        retry_options=types.HttpRetryOptions(attempts=1)
    )
)

print("Connecting to Gemini...")
print(f"Using model: {model_name}")

# Start measuring API response time
start_time = time.perf_counter()

# Send a test request
response = client.models.generate_content(
    model=model_name,
    contents="Hello Gemini! Introduce yourself in one sentence."
)

# Calculate response time
elapsed_time = time.perf_counter() - start_time

# Display the response
print("\nGemini Response:")
print(response.text)

# Display API response time
print(f"\nGemini API response time: {elapsed_time:.2f} seconds")
