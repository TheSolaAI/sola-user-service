from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from sqlalchemy.exc import OperationalError
from functools import wraps
from time import sleep

from app.core.security import verify_privy_jwt
from app.db.session import get_session
from app.services.auth_service import auto_add_or_update_user

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_db():
    max_retries = 3
    retry_delay = 1  # Initial delay in seconds
    
    for attempt in range(max_retries):
        with get_session() as session:
            try:
                yield session
                break
            except OperationalError as e:
                if attempt == max_retries - 1:
                    raise e
                sleep_time = retry_delay * (2 ** attempt)  # Exponential backoff
                sleep(sleep_time)
            except Exception as e:
                raise e

def get_current_user(
    token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
):
    payload = verify_privy_jwt(token)
    user = auto_add_or_update_user(db, payload)
    return user
