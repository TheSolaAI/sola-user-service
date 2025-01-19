import os

from corsheaders.defaults import default_headers

from . import BASE_DIR, env

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

SECRET_KEY = env("SECRET_KEY")

DEBUG = True


settings = env("DJANGO_SETTINGS_MODULE")

ALLOWED_HOSTS = ["*"]

CORS_ALLOWED_ORIGINS = ["*"]

CSRF_TRUSTED_ORIGINS = ["*"]

INTERNAL_IPS = ["127.0.0.1"]

HOSTED_DOMAIN = env("HOSTED_DOMAIN")

CORS_ALLOW_CREDENTIALS = True

CORS_ALLOW_HEADERS = list(default_headers) + [
    "x-password-reset-key",
    "X-CSRFToken",
    "Authorization",
    "X-Firebase-AppCheck",
    "X-API-Version",
]

CORS_EXPOSE_HEADERS = ["X-CSRFToken"]

CSRF_COOKIE_SAMESITE = "None"

SESSION_COOKIE_SAMESITE = "None"

CSRF_USE_SESSIONS = False

CORS_ALLOW_METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"]

ROOT_URLCONF = "tdfa.urls"

SITE_ID = 1

WSGI_APPLICATION = "tdfa.wsgi.application"

ASGI_APPLICATION = "tdfa.asgi.application"

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Kolkata"

USE_I18N = True

USE_TZ = True

AUTH_USER_MODEL = "authw.User"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LOGIN_REDIRECT_URL = "/"

APPEND_SLASH = False

PHONENUMBER_DEFAULT_REGION = "IN"
