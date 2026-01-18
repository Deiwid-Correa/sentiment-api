from fastapi import APIRouter
from app.api.v3.schemas import AnalyzeRequest, AnalyzeResponse
from app.core.sentiment_engine import analyze_text

router = APIRouter(prefix="/v3", tags=["v3"])


@router.post("/analyze", response_model=AnalyzeResponse)
def analyze(request: AnalyzeRequest):
    return analyze_text(request.text)
