from django.db import models

from apps.authw.models import User


class ChatRoom(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    session_id = models.CharField(max_length=100)
    agent_id = models.PositiveSmallIntegerField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="chat_rooms")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ChatMessage(models.Model):
    message = models.JSONField()
    room = models.ForeignKey(
        ChatRoom, on_delete=models.CASCADE, related_name="messages"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
