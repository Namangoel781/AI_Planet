"""Application startup and shutdown events."""
from fastapi import FastAPI
from app.core.openai_client import create_openai_client


async def init_openai_client():
    """Initialize the OpenAI client globally."""
    from app.core.openai_client import client
    import sys
    sys.modules['app.core.openai_client'].client = await create_openai_client()


async def close_openai_client():
    """Close the OpenAI client connection."""
    from app.core.openai_client import client
    if client and client.http_client:
        await client.http_client.aclose()


def create_start_app_handler(app: FastAPI):
    """Create start app handler."""
    async def start_app() -> None:
        await init_openai_client()
    return start_app


def create_stop_app_handler(app: FastAPI):
    """Create stop app handler."""
    async def stop_app() -> None:
        await close_openai_client()
    return stop_app
