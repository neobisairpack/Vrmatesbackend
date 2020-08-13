from rest_framework import serializers

from .models import *
from users.serializers import UserSerializer


class DeliveryImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryImage
        fields = '__all__'


class DeliverySerializer(serializers.ModelSerializer):
    requester = serializers.HiddenField(default=serializers.CurrentUserDefault())
    images = DeliveryImagesSerializer(source='image_set', many=True, read_only=True)

    class Meta:
        model = Delivery
        fields = '__all__'

    def create(self, validated_data):
        images_data = self.context.get('view').request.FILES
        post = Delivery.objects.create(
            requester=self.requester,
            pickup_location=validated_data.get('pickup_location'),
            drop_off_location=validated_data.get('pickup_location'),
            deadline=validated_data.get('deadline'),
            status=validated_data.get('status'),
            title=validated_data.get('title'),
            text=validated_data.get('text'),
        )
        for image_data in images_data.values():
            DeliveryImage.objects.create(post=post, image=image_data)
        return post


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


class PickUpImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PickUpImage
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


class HostingImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = HostingImage
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


class RequestProvideDeliverySerializer(serializers.ModelSerializer):
    requester = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = RequestProvideDelivery
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


class RequestProvidePickUpSerializer(serializers.ModelSerializer):
    requester = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = RequestProvidePickUp
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


class RequestProvideHostingSerializer(serializers.ModelSerializer):
    requester = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = RequestProvideHosting
        fields = '__all__'
