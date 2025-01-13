from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class User(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    connect_wallet: Mapped[str] = mapped_column(String, nullable=True)
    wallet_provider: Mapped[str] = mapped_column(String, nullable=True)
    settings: Mapped["UserSettings"] = relationship(
        "UserSettings", back_populates="user"
    )


class UserSettings(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("users.id"), nullable=False
    )
    theme: Mapped[str] = mapped_column(String, nullable=False, default="system")
    voice_preference: Mapped[str] = mapped_column(
        String, nullable=False, default="voice1"
    )
    emotion_choices: Mapped[dict] = mapped_column(JSONB, nullable=False, default=dict)
    user: Mapped["User"] = relationship("User", back_populates="settings")
