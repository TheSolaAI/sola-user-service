DJANGO_INBUILT_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
]

THIRD_PARTY_APPS = [
    "rest_framework",
    "rest_framework.authtoken",
    "drf_spectacular",
    "corsheaders",
    "django_filters",
    "drf_standardized_errors",
    "fcm_django",
]

HEALTH_CHECK_APPS = [
    "health_check",
    "health_check.db",
]

MY_APPS = [
    # "apps.core",
    "apps.authw",
]

DJANGO_CLEANUP = ["django_cleanup.apps.CleanupConfig"]
