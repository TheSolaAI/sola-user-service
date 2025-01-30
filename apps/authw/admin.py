# from django.contrib import admin

# from .models import User, UserSettings


# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = (
#         "id",
#         "username",
#         "privy_wallet_address",
#         "wallet_address",
#         "wallet_provider",
#     )
#     search_fields = ("username", "privy_wallet_address", "wallet_address")
#     list_filter = ("wallet_provider",)
#     readonly_fields = ("id",)


# @admin.register(UserSettings)
# class UserSettingsAdmin(admin.ModelAdmin):
#     list_display = ("id", "user", "theme", "voice_preference", "emotion_choice")
#     search_fields = ("user__username", "theme", "voice_preference", "emotion_choice")
#     list_filter = ("theme",)
#     readonly_fields = ("id", "user")
