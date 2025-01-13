import jwt
from fastapi import HTTPException
from jwt import PyJWKClient

from app.core.config import settings


def verify_privy_jwt(token: str):
    try:
        if not settings.PRIVY_JWKS_URL:
            raise HTTPException(status_code=500, detail="PRIVY_JWKS_URL is not set")
        jwks_client = PyJWKClient(settings.PRIVY_JWKS_URL)
        signing_key = jwks_client.get_signing_key_from_jwt(token)
        payload = jwt.decode(
            token,
            signing_key.key,
            algorithms=["ES256"],
            audience=settings.PRIVY_APP_ID,
            issuer="privy.io",
        )
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")
