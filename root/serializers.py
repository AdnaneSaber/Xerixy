from .models import Page, PageContent, PhoneClick, ExternalTools, Service, Theme
from rest_framework import serializers


class PhoneSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PhoneClick
        fields = ["__all__"]


class ExternalToolsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ExternalTools
        fields = ["status"]


class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageContent
        fields = '__all__'


class ThemeSerializer(serializers.ModelSerializer):
    # banner_image = serializers.ImageField(source='banner.banner_image')
    banner = serializers.StringRelatedField(many=True)  
    class Meta:
        model = Theme
        fields = ['banner']
        depth = 2
