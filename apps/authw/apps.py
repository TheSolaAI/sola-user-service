from django.apps import AppConfig


class AuthwConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.authw"

    def ready(self):
        import apps.authw.signals  # noqa
        import apps.authw.extension  # noqa
