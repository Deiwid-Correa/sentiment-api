from fastapi import FastAPI
from slowapi.errors import RateLimitExceeded

##from app.api.v1.routes import router as v1_router
from app.api.v2.routes import router as v2_router
from app.api.v3.routes import router as v3_router

from app.core.security.cors import setup_cors
from app.core.security.headers import security_headers
from app.core.security.rate_limit import limiter, rate_limit_exceeded_handler


app = FastAPI(title="Sentiment API")

# =========================
# Rate Limiting (FORMA CORRECTA)
# =========================
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, rate_limit_exceeded_handler)

# =========================
# Seguridad
# =========================
setup_cors(app)
security_headers(app)

# =========================
# Routers
# =========================
##app.include_router(v1_router)
app.include_router(v2_router)
app.include_router(v3_router)
