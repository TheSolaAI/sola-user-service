from sqlmodel import Session, create_engine
from sqlalchemy.pool import QueuePool
from contextlib import contextmanager
from typing import Generator

from app.core.config import settings

if not settings.SQLALCHEMY_DATABASE_URL:
    raise ValueError("SQLALCHEMY_DATABASE_URL is not set")

engine = create_engine(
    settings.SQLALCHEMY_DATABASE_URL,
    poolclass=QueuePool,
    pool_size=10,
    max_overflow=20,
    pool_timeout=30,
    pool_recycle=1800,
    pool_pre_ping=True,
)

@contextmanager
def get_session() -> Generator[Session, None, None]:
    session = Session(engine)
    try:
        yield session
    finally:
        session.close()

def SessionLocal():
    return Session(engine)
