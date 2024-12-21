from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List
import os


class Settings(BaseSettings):
    PROJECT_NAME: str = "PDF Q&A API"
    OPENAI_API_KEY: str
    # Simplified Postgresql path
    DATABASE_URL: str = "Provide your Database URL"
    CORS_ORIGINS: List[str] = ["http://localhost:5173"]
    UPLOAD_DIR: str = "uploads"
    BASE_DIR: str = os.path.dirname(os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))))

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
