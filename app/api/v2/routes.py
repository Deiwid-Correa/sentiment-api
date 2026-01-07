from fastapi import APIRouter, Depends
from app.schemas import TextoEntrada, ErrorResponse
from app.services.sentiment_service_v2 import analizar_v2
from typing import Union

router = APIRouter(
    prefix="/v2",
    tags=["v2"]
)

@router.get("/status")
def status_v2():
    return {
        "version": "v2",
        "status": "En desarrollo"
    }

@router.post(
    "/analyze",
    response_model=Union[dict, ErrorResponse]
)
def analyze_v2(payload: TextoEntrada):
    return analizar_v2(payload.text)
