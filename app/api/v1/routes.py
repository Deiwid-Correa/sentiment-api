from fastapi import APIRouter, Depends, Request
from slowapi import Limiter
from slowapi.util import get_remote_address

from app.schemas import TextoEntrada, RespuestaSentimiento
from app.services.sentiment_service import analizar
from app.security import validar_api_key

# Limiter local (correcto para pytest y prod)
limiter = Limiter(key_func=get_remote_address)

router = APIRouter(prefix="/v1", tags=["v1"])

@router.post("/analyze", response_model=RespuestaSentimiento)
@limiter.limit("5/minute")
def analyze_sentiment(
    request: Request,
    data: TextoEntrada,                    # 📦 BODY (SIN Depends)
    _: str = Depends(validar_api_key)      # 🔐 API KEY
):
    return analizar(data.text)
