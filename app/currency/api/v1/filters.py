import django_filters
from django_filters import FilterSet
from currency.models import Rate, Source


class RateFilter(django_filters.FilterSet):
    class Meta:
        model = Rate
        fields = {
            "buy": ("gt", "gte", "lt", "lte", "exact"),
            "sell": ("gt", "gte", "lt", "lte", "exact"),
            "currency": ("exact",),
        }
