from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr


class UserOut(UserBase):
    id: int
    connect_wallet: str | None
    wallet_provider: str | None

    class Config:
        from_attributes = True


class UserSettings(BaseModel):
    user_id: int
    theme: str = "system"
    voice_preference: str = "voice1"
    emotion_choices: dict = {}

    class Config:
        from_attributes = True
