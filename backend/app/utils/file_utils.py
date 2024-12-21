import os
from app.core.config import settings


def ensure_upload_dir():
    """Ensure the upload directory exists."""
    os.makedirs(settings.UPLOAD_DIR, exist_ok=True)


def get_file_path(filename: str) -> str:
    """Get the full file path for a given filename."""
    return os.path.join(settings.UPLOAD_DIR, filename)
