from .base import *  # noqa: F403
from .services.https import *  # noqa: F403
from .services.sentry import *  # noqa: F403

# from .services.cache import *  # noqa: F403

# rest_framework settings
REST_FRAMEWORK["DEFAULT_RENDERER_CLASSES"] = [  # noqa: F405
    "rest_framework.renderers.JSONRenderer"
]
