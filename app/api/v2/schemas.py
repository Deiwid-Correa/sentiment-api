from pydantic import BaseModel
from typing import Optional


class AnalyzeRequest(BaseModel):
    text: str


class AnalyzeResponse(BaseModel):
    texto: str
    sentimiento: str
    confianza: Optional[float] = None
    explicacion: Optional[str] = None
