from pydantic import BaseModel


class UserBase(BaseModel):
    pass


class UserOut(UserBase):
    id: str
    privy_wallet_id: str | None = None
    wallet_id: str | None = None
    wallet_provider: str | None = None

    class Config:
        from_attributes = True


class UserSettings(BaseModel):
    theme: str | None = None
    voice_preference: str | None = None
    emotion_choices: str | None = None

    class Config:
        from_attributes = True


class UserCreate(BaseModel):
    privy_wallet_id: str | None = None
    wallet_id: str | None = None
    wallet_provider: str | None = None
