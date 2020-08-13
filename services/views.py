from django.http import Http404
from rest_framework import viewsets, status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.exceptions import ParseError
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import *


class DeliveryViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated, )
    queryset = Delivery.objects.filter(is_checked=True)
    serializer_class = DeliverySerializer

    def list(self, request, *args, **kwargs):
        service = self.queryset.all()
        serializer = DeliveryReadableSerializer(service, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request):
        pk = request.data.get('id', None)
        if pk is None:
            raise ParseError('Service id is required.')

        try:
            service = self.queryset.get(id=pk)
        except Delivery.DoesNotExist:
            raise Http404
        else:
            service.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


class DeliveryImageViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = DeliveryImage.objects.all()
    serializer_class = DeliveryImagesSerializer

    def get(self):
        image = self.queryset.all()
        serializer = self.serializer_class(image, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request):
        pk = request.data.get('id', None)
        if pk is None:
            raise ParseError('Service id is required.')

        try:
            image = self.queryset.get(id=pk)
        except DeliveryImage.DoesNotExist:
            raise Http404
        else:
            image.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


class RequestDeliveryViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = RequestDelivery.objects.all()
    serializer_class = RequestDeliverySerializer

    def list(self, request, *args, **kwargs):
        service = self.queryset.all()
        serializer = RequestDeliveryReadableSerializer(service, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request):
        pk = request.data.get('id', None)
        if pk is None:
            raise ParseError('Service id is required.')

        try:
            service = self.queryset.get(id=pk)
        except RequestDelivery.DoesNotExist:
            raise Http404
        else:
            service.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


class PickUpViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = PickUp.objects.filter(is_checked=True)
    serializer_class = PickUpSerializer

    def list(self, request, *args, **kwargs):
        service = self.queryset.all()
        serializer = PickUpReadableSerializer(service, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request):
        pk = request.data.get('id', None)
        if pk is None:
            raise ParseError('Service id is required.')

        try:
            service = self.queryset.get(id=pk)
        except PickUp.DoesNotExist:
            raise Http404
        else:
            service.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


class PickUpImageViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated, )
    queryset = PickUpImage.objects.all()
    serializer_class = PickUpImagesSerializer

    def get(self):
        image = self.queryset.all()
        serializer = self.serializer_class(image, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request):
        pk = request.data.get('id', None)
        if pk is None:
            raise ParseError('Service id is required.')

        try:
            image = self.queryset.get(id=pk)
        except PickUpImage.DoesNotExist:
            raise Http404
        else:
            image.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


class RequestPickUpViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = RequestPickUp.objects.all()
    serializer_class = RequestPickUpSerializer

    def list(self, request, *args, **kwargs):
        service = self.queryset.all()
        serializer = RequestPickUpReadableSerializer(service, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request):
        pk = request.data.get('id', None)
        if pk is None:
            raise ParseError('Service id is required.')

        try:
            service = self.queryset.get(id=pk)
        except RequestPickUp.DoesNotExist:
            raise Http404
        else:
            service.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


class HostingViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Hosting.objects.filter(is_checked=True)
    serializer_class = HostingSerializer

    def list(self, request, *args, **kwargs):
        service = self.queryset.all()
        serializer = HostingReadableSerializer(service, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request):
        pk = request.data.get('id', None)
        if pk is None:
            raise ParseError('Hosting id is required.')

        try:
            hosting = self.queryset.get(id=pk)
        except Hosting.DoesNotExist:
            raise Http404
        else:
            hosting.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


class HostingImageViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated, )
    queryset = HostingImage.objects.all()
    serializer_class = HostingImagesSerializer

    def get(self):
        image = self.queryset.all()
        serializer = self.serializer_class(image, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request):
        pk = request.data.get('id', None)
        if pk is None:
            raise ParseError('Service id is required.')

        try:
            image = self.queryset.get(id=pk)
        except HostingImage.DoesNotExist:
            raise Http404
        else:
            image.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


class RequestHostingViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = RequestHosting.objects.all()
    serializer_class = RequestHostingSerializer

    def list(self, request, *args, **kwargs):
        service = self.queryset.all()
        serializer = RequestHostingReadableSerializer(service, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request):
        pk = request.data.get('id', None)
        if pk is None:
            raise ParseError('Service id is required.')

        try:
            service = self.queryset.get(id=pk)
        except RequestHosting.DoesNotExist:
            raise Http404
        else:
            service.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


class SupportViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Support.objects.all()
    serializer_class = SupportSerializer

    def list(self, request, *args, **kwargs):
        support = self.queryset.all()
        serializer = self.serializer_class(support, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request):
        pk = request.data.get('id', None)
        if pk is None:
            raise ParseError('Id is required')

        try:
            support = self.queryset.get(id=pk)
        except Support.DoesNotExist:
            raise Http404
        else:
            support.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


class ProvideDeliveryViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = ProvideDelivery.objects.filter(is_checked=True)
    serializer_class = ProvideDeliverySerializer

    def list(self, request, *args, **kwargs):
        service = self.queryset.all()
        serializer = ProvideDeliveryReadableSerializer(service, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request):
        pk = request.data.get('id', None)
        if pk is None:
            raise ParseError('Service id is required.')

        try:
            service = self.queryset.get(id=pk)
        except ProvideDelivery.DoesNotExist:
            raise Http404
        else:
            service.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


class RequestProvideDeliveryViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = RequestProvideDelivery.objects.all()
    serializer_class = RequestProvideDeliverySerializer

    def list(self, request, *args, **kwargs):
        service = self.queryset.all()
        serializer = RequestProvideDeliverySerializer(service, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request):
        pk = request.data.get('id', None)
        if pk is None:
            raise ParseError('Service id is required.')

        try:
            service = self.queryset.get(id=pk)
        except RequestProvideDelivery.DoesNotExist:
            raise Http404
        else:
            service.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


class ProvidePickUpViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = ProvidePickUp.objects.filter(is_checked=True)
    serializer_class = ProvidePickUpSerializer

    def list(self, request, *args, **kwargs):
        service = self.queryset.all()
        serializer = ProvidePickUpReadableSerializer(service, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data, user=request.user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request):
        pk = request.data.get('id', None)
        if pk is None:
            raise ParseError('Service id is required.')

        try:
            service = self.queryset.get(id=pk)
        except ProvidePickUp.DoesNotExist:
            raise Http404
        else:
            service.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


class RequestProvidePickUpViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = RequestProvidePickUp.objects.all()
    serializer_class = RequestProvidePickUpSerializer

    def list(self, request, *args, **kwargs):
        service = self.queryset.all()
        serializer = RequestProvidePickUpSerializer(service, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request):
        pk = request.data.get('id', None)
        if pk is None:
            raise ParseError('Service id is required.')

        try:
            service = self.queryset.get(id=pk)
        except RequestProvidePickUp.DoesNotExist:
            raise Http404
        else:
            service.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


class ProvideHostingViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated, )
    queryset = ProvideHosting.objects.filter(is_checked=True)
    serializer_class = ProvideHostingSerializer

    def list(self, request, *args, **kwargs):
        service = self.queryset.all()
        serializer = ProvideHostingReadableSerializer(service, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request):
        pk = request.data.get('id', None)
        if pk is None:
            raise ParseError('ProvideHosting id is required.')

        try:
            provide_hosting = self.queryset.get(id=pk)
        except ProvideHosting.DoesNotExist:
            raise Http404
        else:
            provide_hosting.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


class RequestProvideHostingViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = RequestProvideHosting.objects.all()
    serializer_class = RequestProvideHostingSerializer

    def list(self, request, *args, **kwargs):
        service = self.queryset.all()
        serializer = RequestProvideHostingSerializer(service, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request):
        pk = request.data.get('id', None)
        if pk is None:
            raise ParseError('Service id is required.')

        try:
            service = self.queryset.get(id=pk)
        except RequestProvideHosting.DoesNotExist:
            raise Http404
        else:
            service.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


class DeliveryFilterListAPIView(ListAPIView):
    queryset = Delivery.objects.filter(is_checked=True)
    serializer_class = DeliveryReadableSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status', 'created']


class PickUpFilterListAPIView(ListAPIView):
    queryset = PickUp.objects.filter(is_checked=True)
    serializer_class = PickUpReadableSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status', 'created']


class HostingFilterListAPIView(ListAPIView):
    queryset = Hosting.objects.filter(is_checked=True)
    serializer_class = HostingReadableSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status', 'created']


class SupportFilterListAPIView(ListAPIView):
    queryset = Support.objects.all()
    serializer_class = SupportReadableSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'date']
