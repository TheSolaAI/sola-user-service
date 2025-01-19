from sqlmodel import Field, Relationship, SQLModel


class UserSettings(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    user_id: str = Field(foreign_key="user.id")
    theme: str | None = Field(default="system")
    voice_preference: str | None = Field(default="voice1")
    emotion_choices: str | None = Field(default="")
    user: "User" = Relationship(back_populates="settings")


class User(SQLModel, table=True):
    id: str = Field(default=None, primary_key=True)
    privy_wallet_id: str | None = Field(default=None)
    wallet_id: str | None = Field(default=None)
    wallet_provider: str | None = Field(default=None)
    settings: UserSettings = Relationship(back_populates="user")
