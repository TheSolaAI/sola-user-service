from rest_framework import serializers

from .models import LimitOrder


class LimitOrderSerializer(serializers.ModelSerializer):
    user_wallet = serializers.PrimaryKeyRelatedField()

    class Meta:
        model = LimitOrder
        fields = [
            "id",
            "user",
            "user_wallet",
            "order_id",
        ]
        read_only_fields = ["id", "user"]

    def validate(self, attrs):
        user = self.context["request"].user
        attrs["user"] = user
        return attrs
