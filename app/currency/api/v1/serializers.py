from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from currency.models import Rate, Source


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = (
            "id",
            "buy",
            "sell",
            "currency",
        )


class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = (
            "id",
            "source_url",
            "name",
        )
