from pydantic import BaseModel, Field, validator
from typing import Optional


class AnalyzeRequest(BaseModel):
    text: str = Field(
        ...,
        min_length=1,
        max_length=500,
        description="Texto en español a analizar"
    )

    @validator("text")
    def text_not_empty(cls, v: str):
        if not v.strip():
            raise ValueError("El texto no puede estar vacío")
        return v


class AnalyzeResponse(BaseModel):
    texto: str
    sentimiento: str
    confianza: float
    version: str
    explicacion: Optional[str] = None
