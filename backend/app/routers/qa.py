from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.deps import get_db
from app.services.qa_service import QAService
from app.models.pdf import PDF
from pydantic import BaseModel

router = APIRouter()


class QuestionRequest(BaseModel):
    pdf_id: int
    question: str


class AnswerResponse(BaseModel):
    answer: str


@router.post("/question", response_model=AnswerResponse)
async def ask_question(
    request: QuestionRequest,
    db: AsyncSession = Depends(get_db)
):
    try:
        pdf = await db.get(PDF, request.pdf_id)
        if not pdf:
            raise HTTPException(status_code=404, detail="PDF not found")

        # Initialize QAService and get the answer
        qa_service = QAService()
        answer = await qa_service.get_answer(request.question, pdf.content)

        return {"answer": answer}
    except Exception as e:
        import logging
        logging.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))
