
"""Carga variables desde .env"""
import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parents[2]
load_dotenv(BASE_DIR / ".env", override=True)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
DB_URL = f"sqlite:///{BASE_DIR / 'build' / 'app.db'}"
