from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class PDFBase(BaseModel):
    filename: str


class PDFCreate(PDFBase):
    pass


class PDF(PDFBase):
    id: int
    file_path: str
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True
