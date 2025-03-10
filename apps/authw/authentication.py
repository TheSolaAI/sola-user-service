from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

from apps.authw.models import User

from .jwt import verify_privy_jwt


class PrivyAuthentication(BaseAuthentication):
    www_authenticate_realm = "api"
    media_type = "application/json"

    def authenticate(self, request):
        token = self.get_token_from_request(request)
        if not token:
            return None

        payload = verify_privy_jwt(token)
        username = payload.get("sub")
        if not username:
            raise AuthenticationFailed("Token payload is missing 'sub' field")

        user, created = User.objects.get_or_create(username=username)
        return (user, token)

    def get_token_from_request(self, request):
        auth_header = request.headers.get("Authorization")
        if auth_header:
            try:
                prefix, token = auth_header.split(" ")
                if prefix.lower() == "bearer":
                    return token
                raise AuthenticationFailed(
                    "Authorization header must start with 'Bearer'"
                )
            except ValueError:
                raise AuthenticationFailed("Invalid Authorization header format")
        return request.COOKIES.get("privy-id-token")

    def authenticate_header(self, request) -> str:
        return "Bearer realm='{}'".format(self.www_authenticate_realm)
