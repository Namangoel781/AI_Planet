import aiofiles
from app.utils.file_utils import ensure_upload_dir, get_file_path
import asyncio
import fitz


class PDFService:
    @staticmethod
    async def extract_text(file_path: str) -> str:
        """Extract text from PDF asynchronously."""
        try:
            text = await asyncio.to_thread(PDFService._sync_extract_text, file_path)
            return text
        except Exception as e:
            raise Exception(f"Error extracting text from PDF: {str(e)}")

    @staticmethod
    def _sync_extract_text(file_path: str) -> str:
        """Synchronous text extraction from PDF."""
        doc = fitz.open(file_path)
        try:
            return "".join(page.get_text() for page in doc)
        finally:
            doc.close()

    @staticmethod
    async def save_pdf(file_content: bytes, filename: str) -> str:
        """Save PDF file to disk asynchronously."""
        ensure_upload_dir()
        file_path = get_file_path(filename)
        try:
            async with aiofiles.open(file_path, "wb") as f:
                await f.write(file_content)
            return file_path
        except Exception as e:
            raise Exception(f"Error saving PDF: {str(e)}")
