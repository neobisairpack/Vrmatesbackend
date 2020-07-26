from rest_framework import serializers

from .models import Service, Hosting, Support
from users.serializers import UserSerializer


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class ServiceReadableSerializer(serializers.ModelSerializer):
    requester = UserSerializer()
    provider = UserSerializer()

    class Meta:
        model = Service
        fields = '__all__'


class HostingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hosting
        fields = '__all__'


class HostingReadableSerializer(serializers.ModelSerializer):
    requester = UserSerializer()
    provider = UserSerializer()

    class Meta:
        model = Hosting
        fields = '__all__'


class SupportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Support
        fields = '__all__'


class SupportReadableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Support
        fields = '__all__'
