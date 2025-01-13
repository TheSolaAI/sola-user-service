import sentry_sdk
from fastapi import FastAPI, Request
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi_migrate import Migrate
from slowapi import Limiter
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from slowapi.util import get_remote_address
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse

from app.api.v1.auth import router as auth_router
from app.core.config import settings
from app.core.logging_config import logger
from app.db.models import SQLModel

sentry_sdk.init(
    dsn=settings.SENTRY_DSN,
    traces_sample_rate=1.0,
    _experiments={
        "continuous_profiling_auto_start": True,
    },
)

app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)

if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

# Trusted Host Middleware
app.add_middleware(TrustedHostMiddleware, allowed_hosts=settings.ALLOWED_HOSTS)

# Rate Limiting Middleware
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter


@app.exception_handler(RateLimitExceeded)
def rate_limit_exceeded_handler(request: Request, exc: RateLimitExceeded):
    return JSONResponse(
        status_code=429,
        content={"detail": "Rate limit exceeded", "retry_after": exc.detail},
    )


app.add_middleware(SlowAPIMiddleware)

app.include_router(auth_router, prefix="/api/v1/auth")


if settings.SQLALCHEMY_DATABASE_URL:
    migrate = Migrate(app, SQLModel, settings.SQLALCHEMY_DATABASE_URL)
else:
    raise ValueError("SQLALCHEMY_DATABASE_URL must be set in the settings")


@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "healthy"}


logger.info("Application startup complete")
