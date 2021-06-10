from .models import PhoneClick,ExternalTools
from rest_framework import serializers

class PhoneSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PhoneClick
        fields = ["__all__"]


class ExternalToolsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ExternalTools
        fields = ["status"]