from django.db import models

from apps.authw.models import User, UserWallets


class LimitOrder(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="limit_orders"
    )
    user_wallet = models.ForeignKey(
        UserWallets, on_delete=models.CASCADE, related_name="limit_orders"
    )
    order_id = models.CharField(max_length=255)
