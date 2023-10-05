from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from currency.models import Rate, Source, ContactUs, RequestResponseLog
from currency.tasks import send_email_contact_us

class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = "__all__"


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

def create(self, validated_data):
    instance = super().create(validated_data)

    send_email_contact_us.delay(validated_data)

    return instance

class LogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestResponseLog
        fields = "__all__"
