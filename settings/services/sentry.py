import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

from . import env

sentry_sdk.init(
    dsn=env("SENTRY_DSN"),  # noqa
    integrations=[
        DjangoIntegration(),
        # CeleryIntegration(
        #     monitor_beat_tasks=True,
        # ),
        # AioHttpIntegration(),
        # RedisIntegration(),
        # LoggingIntegration(),
    ],
    send_default_pii=True,
    traces_sample_rate=1.0,
    profiles_sample_rate=1.0,
    auto_session_tracking=True,
    _experiments={
        "continuous_profiling_auto_start": True,
    },
    environment=env("ENVIRONMENT"),
)
