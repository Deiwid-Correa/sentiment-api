from fastapi import APIRouter
from app.api.v1.schemas import AnalyzeRequest, AnalyzeResponse
from app.services.sentiment_service import analyze_text

router = APIRouter(prefix="/v1", tags=["v1"])

@router.post("/analyze", response_model=AnalyzeResponse)
def analyze(request: AnalyzeRequest):
    result = analyze_text(request.text)

    sentimiento = result["sentimiento"]
    if sentimiento == "neutro":
        sentimiento = "neutral"

    return {
        "texto": request.text,
        "sentimiento": sentimiento
    }
