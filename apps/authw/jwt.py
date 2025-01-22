from datetime import timedelta

import jwt
from django.conf import settings
from jwt import PyJWKClient
from rest_framework.exceptions import AuthenticationFailed, NotAuthenticated


def verify_privy_jwt(token: str):
    try:
        if not settings.PRIVY_JWKS_URL:
            raise NotAuthenticated(detail="PRIVY_JWKS_URL is not set")
        jwks_client = PyJWKClient(settings.PRIVY_JWKS_URL)
        signing_key = jwks_client.get_signing_key_from_jwt(token)
        payload = jwt.decode(
            token,
            signing_key.key,
            algorithms=["ES256"],
            audience=settings.PRIVY_APP_ID,
            issuer="privy.io",
            leeway=timedelta(hours=30),
        )
        return payload
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed(detail="Token has expired")
    except jwt.InvalidTokenError:
        raise AuthenticationFailed(detail="Invalid token")
