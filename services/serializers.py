from rest_framework import serializers

from .models import Service, Hosting
from users.serializers import UserSerializer


class ServiceSerializer(serializers.ModelSerializer):
    requester = UserSerializer()
    provider = UserSerializer()

    class Meta:
        model = Service
        fields = '__all__'


class HostingSerializer(serializers.ModelSerializer):
    requester = UserSerializer()
    provider = UserSerializer()

    class Meta:
        model = Hosting
        fields = '__all__'

