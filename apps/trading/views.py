from rest_framework import mixins, viewsets

from .models import LimitOrder
from .serializers import LimitOrderSerializer


class LimitOrderViewSet(
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
):
    serializer_class = LimitOrderSerializer

    def get_queryset(self):
        user = self.request.user
        return LimitOrder.objects.filter(user=user)
