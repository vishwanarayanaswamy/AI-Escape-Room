
import os
from pathlib import Path

from dotenv import load_dotenv
from google import genai

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
client = genai.Client(api_key=api_key)

print("Connecting to Gemini...")
print(f"Using model: {model_name}")

# Send a test request
response = client.models.generate_content(
    model=model_name,
    contents="Hello Gemini! Introduce yourself in one sentence."
)

# Display the response
print("\nGemini Response:")
print(response.text)
