from fastapi import HTTPException, status
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.exc import OperationalError
from time import sleep
from sqlalchemy.orm import Session

from app.db.models import User, UserSettings

    max_retries = 3
    retry_delay = 1  # Initial delay in seconds
    
    for attempt in range(max_retries):
        try:
            user = db.query(User).filter(User.id == user_data["sub"]).first()
            if user:
                user.privy_wallet_id = user_data.get("privy_wallet_id", user.privy_wallet_id)
                user.wallet_id = user_data.get("wallet_id", user.wallet_id)
                user.wallet_provider = user_data.get("wallet_provider", user.wallet_provider)
            else:
                user = User(
                    id=user_data["sub"],
                    privy_wallet_id=user_data.get("privy_wallet_id") or None,
                    wallet_id=user_data.get("wallet_id") or None,
                    wallet_provider=user_data.get("wallet_provider") or None,
                )
                settings = UserSettings(user_id=user.id)
                db.add(user)
                db.add(settings)
            
            db.commit()
            db.refresh(user)
            return user
        except OperationalError as e:
            db.rollback()
            if attempt == max_retries - 1:
                raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, 
                                 detail="Database connection error")
            sleep(retry_delay * (2 ** attempt))  # Exponential backoff
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
                             detail=str(e))

            db.commit()

            persisted_user = db.query(User).filter(User.id == user_data["sub"]).first()
            if not persisted_user:
                raise HTTPException(status_code=500, detail="Failed to create user")
            return persisted_user

        except SQLAlchemyError as e:
            db.rollback()
            raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

    return user


def update_user_settings(db: Session, user_id: str, settings: dict) -> UserSettings:
    user_settings = db.query(UserSettings).filter_by(user_id=user_id).first()
    if user_settings:
        if settings.get("theme") is not None:
            user_settings.theme = settings["theme"]
        if settings.get("voice_preference") is not None:
            user_settings.voice_preference = settings["voice_preference"]
        if settings.get("emotion_choices") is not None:
            user_settings.emotion_choices = settings["emotion_choices"]
    else:
        user_settings = UserSettings(
            user_id=user_id,
            theme=settings.get("theme", "system"),
            voice_preference=settings.get("voice_preference", "ash"),
            emotion_choices=settings.get(
                "emotion_choices", "highly energetic and cheerfully enthusiastic"
            ),
        )
        db.add(user_settings)
    db.commit()
    db.refresh(user_settings)
    return user_settings


def get_user_settings(db: Session, user_id: str) -> UserSettings:
    user_settings = db.query(UserSettings).filter_by(user_id=user_id).first()
    if user_settings is None:
        raise HTTPException(status_code=404, detail="User settings not found")
    return user_settings
