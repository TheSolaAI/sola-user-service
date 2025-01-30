from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.authw.views import (
    UserListViewSet,
    UserRegisterViewSet,
    UserSettingsViewSet,
    UserWalletViewSet,
)

router = DefaultRouter()
router.register("auth/register", UserRegisterViewSet, basename="users_register")
router.register("auth/user", UserListViewSet, basename="users")
router.register("auth/settings", UserSettingsViewSet, basename="settings")
router.register("auth/wallet", UserWalletViewSet, basename="wallets")
urlpatterns = [
    path(
        "v1/auth/settings/update/",
        UserSettingsViewSet.as_view({"patch": "custom_partial_update"}),
        name="user-settings-partial-update",
    ),
    path("v1/", include(router.urls)),
]
