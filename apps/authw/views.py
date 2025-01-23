from django.db.models.query import QuerySet
from drf_spectacular.utils import extend_schema
from rest_framework import mixins, permissions, response, status, viewsets

from apps.authw.models import User
from apps.authw.serializers import UserRegisterSerializer, UserSettingsSerializer


class UserRegisterViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = UserRegisterSerializer
    queryset = User.objects.all()


class UserListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self) -> QuerySet:
        user = self.request.user
        return User.objects.filter(user=user)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        serializer = self.get_serializer(queryset.first())
        return response.Response(serializer.data)


class UserSettingsViewSet(
    mixins.ListModelMixin, viewsets.GenericViewSet, mixins.UpdateModelMixin
):
    serializer_class = UserSettingsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self) -> QuerySet:
        user = self.request.user
        return User.objects.filter(user=user)

    @extend_schema(exclude=True)
    def update(self, request, *args, **kwargs):
        if request.method == "PUT":
            return response.Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super().update(request, *args, **kwargs)

    @extend_schema(responses=UserSettingsSerializer)
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        serializer = self.get_serializer(queryset.first())
        return response.Response(serializer.data)
