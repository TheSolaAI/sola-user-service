from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter

from .views import ChatMessageViewSet, ChatRoomViewSet

router = DefaultRouter()
router.register("v1/chatrooms", ChatRoomViewSet, basename="chatroom")

chatrooms_router = NestedDefaultRouter(router, "v1/chatrooms", lookup="room")
chatrooms_router.register("messages", ChatMessageViewSet, basename="chatroom-messages")

urlpatterns = [
    path("", include(router.urls)),
    path("", include(chatrooms_router.urls)),
]
