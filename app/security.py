from typing import Optional
from fastapi import Header, HTTPException
from app.config import API_KEY


def validar_api_key(
    x_api_key: Optional[str] = Header(default=None, alias="x-api-key")
):
    if x_api_key is None:
        raise HTTPException(
            status_code=401,
            detail="API Key requerida"
        )

    if x_api_key != API_KEY:
        raise HTTPException(
            status_code=401,
            detail="API Key inválida"
        )

    return x_api_key
