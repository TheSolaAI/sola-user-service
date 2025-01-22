from rest_framework import serializers

from .models import ChatMessage, ChatRoom


class ChatRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatRoom
        fields = [
            "id",
            "name",
            "session_id",
            "user",
        ]
        read_only_fields = ["id", "user"]


class ChatMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMessage
        fields = [
            "id",
            "message",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]
