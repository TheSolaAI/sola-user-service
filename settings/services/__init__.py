import os
from pathlib import Path

import environ

BASE_DIR = Path(__file__).resolve().parent.parent.parent

env = environ.Env(
    DEBUG=(bool, False),
    ENVIRONMENT=(str, None),
)

try:
    env.read_env(env_file=os.path.join(BASE_DIR, ".env"))  # nosec
except Exception:  # nosec
    pass  # nosec

if env("ENVIRONMENT") is None:
    raise Exception("Environment variables not set.")

if (env("ENVIRONMENT") == "production") and (
    env("DJANGO_SETTINGS_MODULE") != "settings.prod"
):
    raise Exception("Invalid DJANGO_SETTINGS_MODULE for production environment.")
