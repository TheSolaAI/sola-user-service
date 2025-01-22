from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.authw.views import UserListViewSet, UserRegisterViewSet, UserSettingsViewSet

router = DefaultRouter()
router.register("auth/register", UserRegisterViewSet, basename="users_register")
router.register("auth/user", UserListViewSet, basename="users")
router.register("auth/settings", UserSettingsViewSet, basename="settings")

urlpatterns = [
    path("v1/", include(router.urls)),
]
