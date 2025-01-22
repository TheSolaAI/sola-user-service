from drf_spectacular.extensions import OpenApiAuthenticationExtension


class PrivyAuthenticationScheme(OpenApiAuthenticationExtension):
    target_class = (
        "apps.authw.authentication.PrivyAuthentication"  # Full path to your class
    )
    name = "BearerAuth"

    def get_security_definition(self, auto_schema):
        return {
            "type": "http",
            "scheme": "bearer",
        }
