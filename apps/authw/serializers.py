from rest_framework import serializers

from .models import User, UserSettings


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "privy_wallet_address",
            "wallet_address",
            "wallet_provider",
        ]
        read_only_fields = [
            "id",
            "username",
        ]

    def create(self, validated_data):
        user = self.context["request"].user
        user, created = User.objects.update_or_create(
            user=user, defaults=validated_data
        )
        return user


class UserSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSettings
        fields = [
            "id",
            "user_id",
            "theme",
            "voice_preference",
            "emotion_choice",
        ]
        read_only_fields = [
            "id",
            "user_id",
        ]
