
from dotenv import load_dotenv
import os

load_dotenv()

GOOGLE_SHEETS_API_KEY = os.getenv("GOOGLE_SHEETS_API_KEY")
if GOOGLE_SHEETS_API_KEY:
    print("API key loaded successfully!")
else:
    print("Failed to load API key. Check your .env file.")
