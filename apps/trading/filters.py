from django_filters import rest_framework as filters

from .models import LimitOrder


class LimitOrderFilterSet(filters.FilterSet):
    user_wallet = filters.ModelChoiceFilter(
        field_name="user_wallet", queryset=LimitOrder.objects.all()
    )

    class Meta:
        model = LimitOrder
        fields = ["user_wallet"]
