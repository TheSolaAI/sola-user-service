from .services.aws import *  # noqa: F403
from .services.db import *  # noqa: F403
from .services.django_defaults import *  # noqa: F403
from .services.drf import *  # noqa: F403
from .services.installed_apps import (
    DJANGO_INBUILT_APPS,
    HEALTH_CHECK_APPS,
    MY_APPS,
    THIRD_PARTY_APPS,
)
from .services.storages import *  # noqa: F403

INSTALLED_APPS = DJANGO_INBUILT_APPS + THIRD_PARTY_APPS + HEALTH_CHECK_APPS + MY_APPS


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "allauth.account.middleware.AccountMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)
