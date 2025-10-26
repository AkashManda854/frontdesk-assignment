from pydantic import BaseModel
from datetime import datetime

class HelpRequestSchema(BaseModel):
    id: str
    question: str
    status: str
    answer: str | None
    created_at: datetime

    class Config:
        orm_mode = True

class KnowledgeSchema(BaseModel):
    id: str
    question: str
    answer: str
    created_at: datetime

    class Config:
        orm_mode = True
