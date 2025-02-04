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
    email = models.EmailField(default=None, null=True, blank=True)
    REQUIRED_FIELDS = []


class UserWallets(models.Model):
    WALLET_PROVIDER_CHOICES = [
        ("privy", "Privy Wallet"),
        ("solflare", "Solflare Wallet"),
        ("phantom", "Phantom Wallet"),
    ]
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="wallets")
    wallet_address = models.CharField(max_length=255)
    wallet_provider = models.CharField(max_length=50, choices=WALLET_PROVIDER_CHOICES)


class UserSettings(models.Model):
    THEME_CHOICES = [
        ("light", "Light"),
        ("dark", "Dark"),
        ("system", "System"),
    ]
    TIER_CHOICES = [
        ("tier1", "Tier 1"),
        ("tier2", "Tier 2"),
        ("tier3", "Tier 3"),
    ]
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="settings")
    theme = models.CharField(max_length=20, default="system", choices=THEME_CHOICES)
    voice_preference = models.CharField(max_length=25, default="ash")
    emotion_choice = models.CharField(
        max_length=255, default="highly energetic and cheerfully enthusiastic"
    )
    credits_remaining = models.IntegerField(default=0)
    tiers = models.CharField(max_length=10, default="tier1", choices=TIER_CHOICES)
