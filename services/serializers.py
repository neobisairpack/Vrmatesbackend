from rest_framework import serializers

from .models import *
from .mixins import ExtraFieldsMixin
from users.models import User
from users.serializers import UserSerializer


class ServiceImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceImage
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer, ExtraFieldsMixin):
    requester = serializers.HiddenField(default=serializers.CurrentUserDefault())
    images = ServiceImagesSerializer(many=True, required=False)

    class Meta:
        model = Service
        fields = ['requester', 'requester_from', 'service_type', 'location', 'preferences',
                  'pickup_location', 'drop_off_location', 'arrive_date', 'deadline',
                  'status', 'title', 'text', 'is_checked', 'provider', 'images']
        extra_fields = ['images']

    def create(self, validated_data):
        images_data = self.context.get('view').request.FILES
        post = Service.objects.create(
            requester=validated_data.get('requester'),
            requester_from=validated_data.get('requester_from'),
            service_type=validated_data.get('service_type'),
            location=validated_data.get('location'),
            preferences=validated_data.get('preferences'),
            pickup_location=validated_data.get('pickup_location'),
            drop_off_location=validated_data.get('drop_off_location'),
            deadline=validated_data.get('deadline'),
            status=validated_data.get('status'),
            title=validated_data.get('title'),
            text=validated_data.get('text'),
        )
        for image_data in images_data.values():
            ServiceImage.objects.create(post=post, image=image_data)
        return post


class ServiceReadableSerializer(serializers.ModelSerializer):
    requester = UserSerializer()
    provider = UserSerializer()

    class Meta:
        model = Service
        fields = '__all__'


class RequestServiceSerializer(serializers.ModelSerializer):
    requester = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = RequestService
        fields = '__all__'


class RequestServiceReadableSerializer(serializers.ModelSerializer):
    service = ServiceReadableSerializer()
    requester = UserSerializer()

    class Meta:
        model = RequestService
        fields = '__all__'


class SupportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Support
        fields = '__all__'


class SupportReadableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Support
        fields = '__all__'


class ProvideServiceImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceImage
        fields = '__all__'


class ProvideServiceSerializer(serializers.ModelSerializer):
    provider = serializers.HiddenField(default=serializers.CurrentUserDefault())
    images = ProvideServiceImagesSerializer(many=True, required=False)

    class Meta:
        model = ProvideService
        fields = ['requester', 'provider_from', 'service_type', 'location', 'preferences',
                  'pickup_location', 'drop_off_location', 'arrive_date', 'deadline',
                  'status', 'title', 'text', 'is_checked', 'provider', 'images']
        extra_fields = ['images']

    def create(self, validated_data):
        images_data = self.context.get('view').request.FILES
        post = ProvideService.objects.create(
            provider=validated_data.get('provider'),
            provider_from=validated_data.get('provider_from'),
            service_type=validated_data.get('service_type'),
            location=validated_data.get('location'),
            preferences=validated_data.get('preferences'),
            pickup_location=validated_data.get('pickup_location'),
            drop_off_location=validated_data.get('drop_off_location'),
            deadline=validated_data.get('deadline'),
            status=validated_data.get('status'),
            title=validated_data.get('title'),
            text=validated_data.get('text'),
        )
        for image_data in images_data.values():
            ProvideServiceImage.objects.create(post=post, image=image_data)
        return post


class ProvideServiceReadableSerializer(serializers.ModelSerializer):
    requester = UserSerializer()
    provider = UserSerializer()

    class Meta:
        model = ProvideService
        fields = '__all__'


class RequestProvideServiceSerializer(serializers.ModelSerializer):
    requester = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = RequestProvideService
        fields = '__all__'
