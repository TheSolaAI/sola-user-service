from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField(
        max_length=150,
        unique=True,
        error_messages={
            "unique": "A user with that username already exists.",
        },
    )
    email = None
    privy_wallet_address = models.CharField(max_length=50, null=True, default=None)
    wallet_address = models.CharField(
        max_length=50, blank=True, null=True, default=None
    )
    wallet_provider = models.CharField(
        max_length=50, blank=True, null=True, default=None
    )


class UserSettings(models.Model):
    THEME_CHOICES = [
        ("light", "Light"),
        ("dark", "Dark"),
        ("system", "System"),
    ]
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="settings")
    theme = models.CharField(max_length=20, default="system", choices=THEME_CHOICES)
    voice_preference = models.CharField(max_length=25, default="ash")
    emotion_choice = models.CharField(
        max_length=255, default="highly energetic and cheerfully enthusiastic"
    )
