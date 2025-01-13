from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.deps import get_current_user, get_db
from app.db.models import User  # Import the User model
from app.schemas.user import UserOut
from app.schemas.user import UserSettings as UserSettingsSchema
from app.services.auth_service import (
    auto_add_or_update_user,
    get_user_settings,
    update_user_settings,
)

router = APIRouter()


@router.post("/register", response_model=UserOut)
def register_user(
    db: Session = Depends(get_db), current_user: User = Depends(get_current_user)
):
    user_data = {
        "sub": current_user.id,
        "connect_wallet": current_user.connect_wallet,
        "wallet_provider": current_user.wallet_provider,
    }
    user = auto_add_or_update_user(db, user_data)
    return user


@router.put("/settings", response_model=UserSettingsSchema)
def update_settings(
    settings_in: UserSettingsSchema,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    settings = update_user_settings(db, current_user.id, settings_in.dict())
    return settings


@router.get("/settings", response_model=UserSettingsSchema)
def get_settings(
    db: Session = Depends(get_db), current_user: User = Depends(get_current_user)
):
    settings = get_user_settings(db, current_user.id)
    if not settings:
        raise HTTPException(status_code=404, detail="Settings not found")
    return settings
