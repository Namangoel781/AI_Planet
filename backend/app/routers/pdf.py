from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.deps import get_db
from app.services.pdf_service import PDFService
from app.models.pdf import PDF
import app.schema.pdf as schemas

router = APIRouter()


@router.post("/upload", response_model=schemas.PDF)
async def upload_pdf(
    file: UploadFile = File(...),
    db: AsyncSession = Depends(get_db)
):
    if not file:
        raise HTTPException(status_code=400, detail="No file uploaded")

    try:

        print(f"Uploaded file: {file.filename}")

        # Save PDF file
        file_content = await file.read()
        file_path = await PDFService.save_pdf(file_content, file.filename)

        # Extract text from PDF
        text_content = await PDFService.extract_text(file_path)

        # Save to database
        pdf = PDF(
            filename=file.filename,
            file_path=file_path,
            content=text_content
        )
        db.add(pdf)
        await db.commit()
        await db.refresh(pdf)

        return pdf
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
