from rest_framework import serializers

from .models import *
from users.serializers import UserSerializer


class DeliverySerializer(serializers.ModelSerializer):
    requester = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Delivery
        fields = '__all__'


class DeliveryReadableSerializer(serializers.ModelSerializer):
    requester = UserSerializer()
    provider = UserSerializer()

    class Meta:
        model = Delivery
        fields = '__all__'


class RequestDeliverySerializer(serializers.ModelSerializer):
    requester = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = RequestDelivery
        fields = '__all__'


class RequestDeliveryReadableSerializer(serializers.ModelSerializer):
    service = DeliveryReadableSerializer()
    requester = UserSerializer()

    class Meta:
        model = RequestDelivery
        fields = '__all__'


class PickUpSerializer(serializers.ModelSerializer):
    requester = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = PickUp
        fields = '__all__'


class PickUpReadableSerializer(serializers.ModelSerializer):
    requester = UserSerializer()
    provider = UserSerializer()

    class Meta:
        model = PickUp
        fields = '__all__'


class RequestPickUpSerializer(serializers.ModelSerializer):
    requester = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = RequestPickUp
        fields = '__all__'


class RequestPickUpReadableSerializer(serializers.ModelSerializer):
    service = PickUpReadableSerializer()
    requester = UserSerializer()

    class Meta:
        model = RequestPickUp
        fields = '__all__'


class HostingSerializer(serializers.ModelSerializer):
    requester = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Hosting
        fields = '__all__'


class HostingReadableSerializer(serializers.ModelSerializer):
    requester = UserSerializer()
    provider = UserSerializer()

    class Meta:
        model = Hosting
        fields = '__all__'


class RequestHostingSerializer(serializers.ModelSerializer):
    requester = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = RequestHosting
        fields = '__all__'


class RequestHostingReadableSerializer(serializers.ModelSerializer):
    service = HostingReadableSerializer()
    requester = UserSerializer()

    class Meta:
        model = RequestHosting
        fields = '__all__'


class SupportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Support
        fields = '__all__'


class SupportReadableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Support
        fields = '__all__'


class ProvideDeliverySerializer(serializers.ModelSerializer):
    provider = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = ProvideDelivery
        fields = '__all__'


class ProvideDeliveryReadableSerializer(serializers.ModelSerializer):
    requester = UserSerializer()
    provider = UserSerializer()

    class Meta:
        model = ProvideDelivery
        fields = '__all__'


class ProvidePickUpSerializer(serializers.ModelSerializer):
    provider = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = ProvidePickUp
        fields = '__all__'


class ProvidePickUpReadableSerializer(serializers.ModelSerializer):
    requester = UserSerializer()
    provider = UserSerializer()

    class Meta:
        model = ProvidePickUp
        fields = '__all__'


class ProvideHostingSerializer(serializers.ModelSerializer):
    provider = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = ProvideHosting
        fields = '__all__'


class ProvideHostingReadableSerializer(serializers.ModelSerializer):
    requester = UserSerializer()
    provider = UserSerializer()

    class Meta:
        model = ProvideHosting
        fields = '__all__'
