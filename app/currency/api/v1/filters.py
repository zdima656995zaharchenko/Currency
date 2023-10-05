import django_filters
from django_filters import FilterSet
from currency.models import Rate, ContactUs


class RateFilter(django_filters.FilterSet):
    class Meta:
        model = Rate
        fields = {
            "buy": ("gt", "gte", "lt", "lte", "exact"),
            "sell": ("gt", "gte", "lt", "lte", "exact"),
            "currency": ("exact",),
        }

class ContactUsFilter(django_filters.FilterSet):
    class Meta:
        model = ContactUs
        fields = {
            'name': ['exact', 'icontains'],
            'created': ['exact', 'gte', 'lte'],
        }