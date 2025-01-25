from django.contrib import admin

from .models import ChatMessage, ChatRoom


@admin.register(ChatRoom)
class ChatRoomAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "session_id", "user", "created_at", "updated_at")
    search_fields = ("name", "session_id", "user__username")
    list_filter = ("created_at", "updated_at")
    readonly_fields = ("created_at", "updated_at")


@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ("id", "room", "created_at", "updated_at")
    search_fields = ("room__name",)
    list_filter = ("created_at", "updated_at")
    readonly_fields = ("created_at", "updated_at")
