from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from currency.models import Rate, Source, ContactUs, RequestResponseLog


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


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = "__all__"


class LogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestResponseLog
        fields = "__all__"
