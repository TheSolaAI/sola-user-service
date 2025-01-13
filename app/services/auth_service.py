from sqlalchemy.orm import Session

from app.db.models import User, UserSettings


def auto_add_or_update_user(db: Session, user_data: dict) -> User:
    user = db.query(User).filter(User.id == user_data["sub"]).first()
    if user:
        user.connect_wallet = user_data.get("connect_wallet", user.connect_wallet)
        user.wallet_provider = user_data.get("wallet_provider", user.wallet_provider)
    else:
        user = User(
            id=user_data["sub"],
            connect_wallet=user_data.get("connect_wallet"),
            wallet_provider=user_data.get("wallet_provider"),
        )
        db.add(user)
    db.commit()
    db.refresh(user)
    return user


def update_user_settings(db: Session, user_id: int, settings: dict) -> UserSettings:
    user_settings = (
        db.query(UserSettings).filter(UserSettings.user_id == user_id).first()
    )
    if user_settings:
        user_settings.theme = settings.get("theme", user_settings.theme)
        user_settings.voice_preference = settings.get(
            "voice_preference", user_settings.voice_preference
        )
        user_settings.emotion_choices = settings.get(
            "emotion_choices", user_settings.emotion_choices
        )
    else:
        user_settings = UserSettings(
            user_id=user_id,
            theme=settings.get("theme", "system"),
            voice_preference=settings.get("voice_preference", "voice1"),
            emotion_choices=settings.get("emotion_choices", {}),
        )
        db.add(user_settings)
    db.commit()
    db.refresh(user_settings)
    return user_settings


def get_user_settings(db: Session, user_id: int) -> UserSettings:
    user_settings = (
        db.query(UserSettings).filter(UserSettings.user_id == user_id).first()
    )
    if user_settings is None:
        raise ValueError("User settings not found")
    return user_settings
