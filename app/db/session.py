from sqlmodel import Session, create_engine

from app.core.config import settings

if not settings.SQLALCHEMY_DATABASE_URL:
    raise ValueError("SQLALCHEMY_DATABASE_URL is not set")

engine = create_engine(settings.SQLALCHEMY_DATABASE_URL)


def SessionLocal():
    return Session(engine)
