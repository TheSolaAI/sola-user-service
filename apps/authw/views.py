from decimal import Decimal

from django.conf import settings
from django.db.models.query import QuerySet
from drf_spectacular.utils import OpenApiExample, extend_schema
from rest_framework import (
    decorators,
    exceptions,
    mixins,
    permissions,
    response,
    status,
    viewsets,
)

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

    def get_queryset(self) -> QuerySet[UserSettings]:
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

    @extend_schema(
        examples=[
            OpenApiExample(
                name="Example",
                value={"credits": 0.001},
                request_only=True,
                response_only=False,
            ),
            OpenApiExample(
                name="Example",
                value={"credits_remaining": 0.001},
                request_only=False,
                response_only=True,
            ),
        ],
    )
    @decorators.action(detail=False, methods=["post"])
    def charge_credits(self, request, *args, **kwargs):
        user_settings = self.get_queryset().first()
        detected_credits = request.data.get("credits", 0.001)
        if detected_credits < 0.001:
            detected_credits = 0.001
        if not user_settings:
            raise exceptions.ValidationError({"detail": "User settings not found."})
        user_settings.credits_remaining -= Decimal(detected_credits)
        user_settings.save()
        return response.Response({"credits_remaining": user_settings.credits_remaining})

    @extend_schema(
        examples=[
            OpenApiExample(
                name="Example",
                value={
                    "credits": 0.001,
                    "signature": "server_signature",
                },
                request_only=True,
                response_only=False,
            ),
            OpenApiExample(
                name="Example",
                value={"credits_remaining": 0.001},
                request_only=False,
                response_only=True,
            ),
        ],
    )
    @decorators.action(detail=False, methods=["post"])
    def recharge_credits(self, request, *args, **kwargs):
        credits = request.data.get("credits", 0.001)
        signature = request.data.get("signature")

        if not signature:
            raise exceptions.PermissionDenied({"detail": "Missing signature field."})
        if not credits:
            raise exceptions.ValidationError({"detail": "Missing Credits field."})

        if str(signature) != str(settings.SECRET_KEY):
            raise exceptions.PermissionDenied({"detail": "Invalid signature."})

        user_settings = self.get_queryset().first()
        if not user_settings:
            raise exceptions.ValidationError({"detail": "User settings not found."})

        user_settings.credits_remaining += Decimal(credits)
        user_settings.save()

        return response.Response({"credits_remaining": user_settings.credits_remaining})


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
