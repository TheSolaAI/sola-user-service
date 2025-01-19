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
    # Set traces_sample_rate to 1.0 to capture 100% of transactions\
    #  for performance monitoring.
    send_default_pii=True,
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100% of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
    auto_session_tracking=True,
    environment=env("ENVIRONMENT"),
)
