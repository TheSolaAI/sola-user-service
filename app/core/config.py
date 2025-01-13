import os

from dotenv import load_dotenv
from pydantic import AnyHttpUrl, field_validator
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    PROJECT_NAME: str = "Sola Auth Service"
    VERSION: str = "1.0.0"
    BACKEND_CORS_ORIGINS: list[AnyHttpUrl] = []
    ALLOWED_HOSTS: list[str] = ["*"]
    SQLALCHEMY_DATABASE_URL: str | None = os.getenv("SQLALCHEMY_DATABASE_URL")
    PRIVY_APP_ID: str | None = os.getenv("PRIVY_APP_ID")
    PRIVY_JWKS_URL: str | None = os.getenv("PRIVY_JWKS_URL")
    SENTRY_DSN: str | None = os.getenv("SENTRY_DSN")

    @field_validator("BACKEND_CORS_ORIGINS", mode="before")
    def assemble_cors_origins(cls, v: str | list[str]) -> list[str] | str:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        if isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()
