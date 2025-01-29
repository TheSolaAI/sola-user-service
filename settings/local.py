from .base import *  # noqa
from .services.aws import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY  # noqa
# from .services.sentry import *  # noqa: F403

# INSTALLED_APPS += [  # noqa
#     "debug_toolbar",
# ]


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    # "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

STORAGES["staticfiles"] = {  # noqa
    "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
}
