import os

from dotenv import load_dotenv

load_dotenv()  # reads .env into environment variables

api_key = os.getenv("API_KEY")
api_url = os.getenv("API_URL", "https://api.example.com")

if not api_key:
    print("No API_KEY found. Copy .env.example to .env and fill it in.")
else:
    masked = api_key[:4] + "*" * (len(api_key) - 8) + api_key[-4:]
    print(f"Loaded API_KEY: {masked}  (length {len(api_key)})")
    print(f"API_URL: {api_url}")