from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

limiter = Limiter(key_func=get_remote_address)

app = FastAPI(
    title="Sentiment Analysis API",
    description="API de análisis de sentimiento en español",
    version="2.0"
)

app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)

@app.exception_handler(RateLimitExceeded)
async def rate_limit_handler(request: Request, exc: RateLimitExceeded):
    return JSONResponse(
        status_code=429,
        content={"detail": "Demasiadas solicitudes. Intenta más tarde."}
    )

# Routers
from app.api.v1.routes import router as v1_router
from app.api.v2.routes import router as v2_router

app.include_router(v1_router)
app.include_router(v2_router)

@app.get("/")
def healthcheck():
    return {"message": "API funcionando correctamente"}
