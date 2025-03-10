from datetime import timedelta

import jwt
from django.conf import settings
from jwt import PyJWKClient
from rest_framework.exceptions import AuthenticationFailed, NotAuthenticated


def verify_privy_jwt(token: str):
    exceptions = []

    # Try to verify with primary Privy configuration
    if settings.PRIVY_JWKS_URL and settings.PRIVY_APP_ID:
        try:
            jwks_client = PyJWKClient(settings.PRIVY_JWKS_URL)
            signing_key = jwks_client.get_signing_key_from_jwt(token)
            payload = jwt.decode(
                token,
                signing_key.key,
                algorithms=["ES256"],
                audience=settings.PRIVY_APP_ID,
                issuer="privy.io",
                leeway=timedelta(days=30),
            )
            return payload
        except (jwt.ExpiredSignatureError, jwt.InvalidTokenError) as e:
            exceptions.append(e)

    # Try to verify with secondary Privy configuration
    if settings.PRIVY_JWKS_URL_2 and settings.PRIVY_APP_ID_2:
        try:
            jwks_client = PyJWKClient(settings.PRIVY_JWKS_URL_2)
            signing_key = jwks_client.get_signing_key_from_jwt(token)
            payload = jwt.decode(
                token,
                signing_key.key,
                algorithms=["ES256"],
                audience=settings.PRIVY_APP_ID_2,
                issuer="privy.io",
                leeway=timedelta(days=30),
            )
            return payload
        except (jwt.ExpiredSignatureError, jwt.InvalidTokenError) as e:
            exceptions.append(e)

    # If we got here, both verifications failed or weren't attempted
    if not exceptions:
        raise NotAuthenticated(detail="No Privy configuration is available")

    # Handle the specific error cases
    if any(isinstance(e, jwt.ExpiredSignatureError) for e in exceptions):
        raise AuthenticationFailed(detail="Token has expired")
    else:
        raise AuthenticationFailed(detail="Invalid token")
