"""OpenAI client configuration module."""
from openai import AsyncOpenAI
from app.core.config import settings
from app.core.http_client import create_http_client

# Initialize the OpenAI client
client = None  # Will be initialized in the startup event


async def create_openai_client() -> AsyncOpenAI:
    """Create and configure the OpenAI client."""
    http_client = await create_http_client()
    return AsyncOpenAI(
        api_key=settings.OPENAI_API_KEY,
        http_client=http_client
    )


async def init_openai_client():
    """Initialize the OpenAI client globally."""
    global client
    client = await create_openai_client()
