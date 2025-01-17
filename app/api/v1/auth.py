from fastapi import APIRouter, Body, Depends, Header, HTTPException
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.core.security import verify_privy_jwt
from app.schemas.user import UserCreate, UserOut
from app.schemas.user import UserSettings as UserSettingsSchema
from app.services.auth_service import (
    auto_add_or_update_user,
    get_user_settings,
    update_user_settings,
)

router = APIRouter()


@router.post("/register", response_model=UserOut)
def register_user(
    user_in: UserCreate = Body(...),
    db: Session = Depends(get_db),
    authorization: str = Header(...),
):
    token = authorization.split(" ")[1]
    payload = verify_privy_jwt(token)
    user_data = {
        "sub": payload["sub"],
        "privy_wallet_id": payload.get("privy_wallet_id"),
        "wallet_id": payload.get("wallet_id"),
        "wallet_provider": payload.get("wallet_provider"),
    }
    user = auto_add_or_update_user(db, user_data)
    return user


@router.patch("/settings", response_model=UserSettingsSchema)
def update_settings(
    settings_in: UserSettingsSchema = Body(...),
    db: Session = Depends(get_db),
    authorization: str = Header(...),
):
    token = authorization.split(" ")[1]
    payload = verify_privy_jwt(token)
    settings = update_user_settings(db, payload["sub"], settings_in.dict())
    return settings


@router.get("/settings", response_model=UserSettingsSchema)
def get_settings(
    db: Session = Depends(get_db),
    authorization: str = Header(...),
):
    token = authorization.split(" ")[1]
    payload = verify_privy_jwt(token)
    settings = get_user_settings(db, payload["sub"])
    if not settings:
        raise HTTPException(status_code=404, detail="Settings not found")
    return settings
