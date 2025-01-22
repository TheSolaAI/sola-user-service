from rest_framework import mixins, pagination, permissions, viewsets

from apps.chat.models import ChatMessage, ChatRoom
from apps.chat.serializers import ChatMessageSerializer, ChatRoomSerializer


class ChatRoomViewSet(
    mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    serializer_class = ChatRoomSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return ChatRoom.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ChatMessageViewSet(
    viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin
):
    serializer_class = ChatMessageSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = pagination.LimitOffsetPagination

    def get_queryset(self):
        return ChatMessage.objects.filter(room__id=self.kwargs["room_pk"]).order_by(
            "-id"
        )
