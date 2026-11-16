"""YTAuto Configuration.

Supports both OpenAI and Ollama (local LLM). By default, Ollama is used.
"""
import os
from typing import List
from dotenv import load_dotenv
load_dotenv()

# OpenAI settings (commented out - using Ollama for now)
# OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
# LLM_MODEL: str = os.getenv("LLM_MODEL", "gpt-4o-mini")
# LLM_TEMPERATURE: float = float(os.getenv("LLM_TEMPERATURE", "0.7"))

# Ollama settings (local LLM)
OLLAMA_BASE_URL: str = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
OLLAMA_MODEL: str = os.getenv("OLLAMA_MODEL", "llama3.2:latest")
OLLAMA_TEMPERATURE: float = float(os.getenv("OLLAMA_TEMPERATURE", "0.7"))

# YouTube API settings
YOUTUBE_API_KEY: str = os.getenv("YOUTUBE_API_KEY", "")
YOUTUBE_CLIENT_ID: str = os.getenv("YOUTUBE_CLIENT_ID", "")
YOUTUBE_CLIENT_SECRET: str = os.getenv("YOUTUBE_CLIENT_SECRET", "")
YOUTUBE_SCOPES: List[str] = ["https://www.googleapis.com/auth/youtube.upload"]

# Web search settings
SEARCH_API_KEY: str = os.getenv("SEARCH_API_KEY", "")

# Workflow settings
CHECKPOINT_DIR: str = os.getenv("WORKFLOW_CHECKPOINT_DIR", "./data/output/checkpoints")
MAX_VIDEO_DURATION_MIN: int = 5
MAX_VIDEO_DURATION_MAX: int = 10
MIN_VIDEOS: int = 5
MAX_VIDEOS: int = 10

# Output directories
DATA_DIR: str = "./data"
TOPICS_DIR: str = "./data/topics"
OUTPUT_DIR: str = "./data/output"

# LLM Instance (Ollama - ChatOllama for chat message interface)
from langchain_ollama import ChatOllama

llm = ChatOllama(
    base_url=OLLAMA_BASE_URL,
    model=OLLAMA_MODEL,
    temperature=OLLAMA_TEMPERATURE,
)

for _d in [DATA_DIR, TOPICS_DIR, OUTPUT_DIR, CHECKPOINT_DIR]:
    os.makedirs(_d, exist_ok=True)


class Config:
    """Configuration constants for YTAuto."""
    OLLAMA_BASE_URL: str = OLLAMA_BASE_URL
    OLLAMA_MODEL: str = OLLAMA_MODEL
    OLLAMA_TEMPERATURE: float = OLLAMA_TEMPERATURE
    YOUTUBE_API_KEY: str = YOUTUBE_API_KEY
    YOUTUBE_CLIENT_ID: str = YOUTUBE_CLIENT_ID
    YOUTUBE_CLIENT_SECRET: str = YOUTUBE_CLIENT_SECRET
    YOUTUBE_SCOPES: List[str] = YOUTUBE_SCOPES
    SEARCH_API_KEY: str = SEARCH_API_KEY
    CHECKPOINT_DIR: str = CHECKPOINT_DIR
    MAX_VIDEO_DURATION_MIN: int = MAX_VIDEO_DURATION_MIN
    MAX_VIDEO_DURATION_MAX: int = MAX_VIDEO_DURATION_MAX
    MIN_VIDEOS: int = MIN_VIDEOS
    MAX_VIDEOS: int = MAX_VIDEOS
    DATA_DIR: str = DATA_DIR
    TOPICS_DIR: str = TOPICS_DIR
    OUTPUT_DIR: str = OUTPUT_DIR

config = Config()
