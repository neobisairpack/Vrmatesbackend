from rest_framework import serializers

from .models import Service, Hosting
from users.serializers import UserSerializer


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'
        exclude = ['is_checked']


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

