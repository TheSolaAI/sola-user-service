from rest_framework import serializers

from .models import User, UserSettings, UserWallets


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
        ]
        read_only_fields = [
            "id",
            "username",
        ]

    def create(self, validated_data):
        user = self.context["request"].user
        user, created = User.objects.update_or_create(
            id=user.id, defaults=validated_data
        )
        return user


class UserSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSettings
        fields = [
            "id",
            "user_id",
            "name",
            "profile_pic",
            "theme",
            "custom_themes",
            "voice_preference",
            "emotion_choice",
            "credits_remaining",
            "tiers",
        ]
        read_only_fields = [
            "id",
            "user_id",
            "credits_remaining",
            "tiers",
        ]


class UserWalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserWallets
        fields = [
            "id",
            "user",
            "wallet_address",
            "wallet_provider",
        ]
        read_only_fields = [
            "id",
            "user",
        ]
