import uvicorn
import asyncio
from app.core.database import engine, Base
import os
from app.core.config import settings


async def init_db():
    """Initialize the database and ensure required directories exist."""
    try:
        # Create uploads directory
        os.makedirs(settings.UPLOAD_DIR, exist_ok=True)
        print(f"Uploads directory created or already exists at: {
              settings.UPLOAD_DIR}")

        # Initialize database tables
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        print("Database initialized successfully.")
    except Exception as e:
        print(f"Failed to initialize the database: {e}")
        raise


if __name__ == "__main__":
    asyncio.run(init_db())  # Initialize database
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
