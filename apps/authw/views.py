from django.db.models.query import QuerySet
from drf_spectacular.utils import extend_schema
from rest_framework import mixins, permissions, response, status, viewsets

from apps.authw.models import User, UserSettings, UserWallets
from apps.authw.serializers import (
    UserRegisterSerializer,
    UserSettingsSerializer,
    UserWalletSerializer,
)


class UserRegisterViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = UserRegisterSerializer
    queryset = User.objects.all()


class UserListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self) -> QuerySet:
        user = self.request.user
        return User.objects.filter(id=user.id)  # type: ignore

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        serializer = self.get_serializer(queryset.first())
        return response.Response(serializer.data)


class UserSettingsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = UserSettingsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self) -> QuerySet:
        if getattr(self, "swagger_fake_view", False):
            return UserSettings.objects.none()
        user = self.request.user
        return UserSettings.objects.filter(user=user)

    @extend_schema(responses=UserSettingsSerializer)
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        serializer = self.get_serializer(queryset.first())
        return response.Response(serializer.data)

    @extend_schema(request=UserSettingsSerializer, responses=UserSettingsSerializer)
    def custom_partial_update(self, request, *args, **kwargs):
        user_settings = self.get_queryset().first()
        serializer = self.get_serializer(user_settings, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data)


class UserWalletViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
):
    serializer_class = UserWalletSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self) -> QuerySet:
        user = self.request.user
        return UserWallets.objects.filter(user=user)

    @extend_schema(exclude=True)
    def update(self, request, *args, **kwargs):
        if request.method == "PUT":
            return response.Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super().update(request, *args, **kwargs)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)
