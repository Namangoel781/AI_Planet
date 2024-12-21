"""HTTP client configuration module."""
import httpx


async def create_http_client() -> httpx.AsyncClient:
    """Create and configure the HTTP client."""
    return httpx.AsyncClient(
        timeout=httpx.Timeout(60.0),
        follow_redirects=True
    )
