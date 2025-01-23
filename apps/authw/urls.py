from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.authw.views import UserListViewSet, UserRegisterViewSet, UserSettingsViewSet

router = DefaultRouter()
router.register("auth/register", UserRegisterViewSet, basename="users_register")
router.register("auth/user", UserListViewSet, basename="users")
router.register("auth/settings", UserSettingsViewSet, basename="settings")

urlpatterns = [
    path(
        "v1/auth/settings/",
        UserSettingsViewSet.as_view({"patch": "custom_partial_update"}),
        name="user-settings-partial-update",
    ),
    path("v1/", include(router.urls)),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
