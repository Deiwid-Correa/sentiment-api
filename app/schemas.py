from pydantic import BaseModel
from typing import Optional


class ErrorResponse(BaseModel):
    error_code: str
    message: str
    trace_id: Optional[str] = None


class TextoEntrada(BaseModel):
    text: str


# 🔹 Contrato v1 (NO tocar)
class RespuestaSentimiento(BaseModel):
    texto: str
    sentimiento: str
    probabilidad: float
    modelo: str


# 🔹 Contrato v2 (NUEVO)
class SentimentResponseV2(BaseModel):
    texto: str
    sentimiento: str
    probabilidad: float
    modelo: str
    trace_id: str
