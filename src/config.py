from pathlib import Path
from dotenv import load_dotenv
import os
from openrouter import OpenRouter

env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(env_path)

model = os.getenv("OPENROUTER_MODEL")
ai_client = OpenRouter(api_key=os.getenv("OPENROUTER_API_KEY"))