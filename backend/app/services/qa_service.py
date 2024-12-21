import openai
from app.core.config import settings
from fastapi import HTTPException


class QAService:
    @staticmethod
    async def get_answer(question: str, pdf_content: str) -> str:
        try:
            # Set the OpenAI API key
            openai.api_key = settings.OPENAI_API_KEY

            # Make the OpenAI API call
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": f"Content:\n{
                        pdf_content}\n\nQuestion: {question}"}
                ],
                max_tokens=150
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"Failed to get answer: {str(e)}"
            )
