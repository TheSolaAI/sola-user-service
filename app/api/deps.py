from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.core.security import verify_privy_jwt
from app.db.session import SessionLocal
from app.services.auth_service import auto_add_or_update_user

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_db():
    db = SessionLocal
    try:
        yield db
    finally:
        db.close()


def get_current_user(
    token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
):
    payload = verify_privy_jwt(token)
    user = auto_add_or_update_user(db, payload)
    return user
