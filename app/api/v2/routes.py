from fastapi import APIRouter, Request
from app.core.security.rate_limit import limiter
from app.api.v2.schemas import AnalyzeRequest, AnalyzeResponse

router = APIRouter(prefix="/v2", tags=["v2"])


@router.post(
    "/analyze",
    response_model=AnalyzeResponse
)
@limiter.limit("10/minute")
async def analyze_text(
    request: Request,          # 🔑 OBLIGATORIO PARA SLOWAPI
    payload: AnalyzeRequest
):
    """
    Analiza el sentimiento de un texto (v2).
    Rate limited: 10 requests por minuto por IP.
    """

    text = payload.text.lower()

    if "bueno" in text or "excelente" in text:
        sentimiento = "positivo"
    elif "malo" in text or "horrible" in text:
        sentimiento = "negativo"
    else:
        sentimiento = "neutro"

    return AnalyzeResponse(
        texto=payload.text,
        sentimiento=sentimiento
    )
