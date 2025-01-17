from pydantic import BaseModel


class UserBase(BaseModel):
    pass


class UserOut(UserBase):
    id: int
    privy_wallet_id: str | None
    wallet_id: str | None
    wallet_provider: str | None

    class Config:
        from_attributes = True


class UserSettings(BaseModel):
    user_id: int
    theme: str = "system"
    voice_preference: str = "voice1"
    emotion_choices: str = ""

    class Config:
        from_attributes = True


class UserCreate(BaseModel):
    privy_wallet_id: str
    wallet_id: str
    wallet_provider: str
