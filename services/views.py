from django.http import Http404
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.exceptions import ParseError
from rest_framework.permissions import IsAuthenticated

from .models import Service, Hosting
from .serializers import (
    ServiceSerializer,
    ServiceReadableSerializer,
    HostingSerializer,
    HostingReadableSerializer
)


class ServiceViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Service.objects.filter(is_checked=True)
    serializer_class = ServiceSerializer

    def list(self, request, *args, **kwargs):
        service = self.queryset.all()
        serializer = ServiceReadableSerializer(service, many=True)
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
        except Service.DoesNotExist:
            raise Http404
        else:
            service.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


class HostingViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Hosting.objects.filter(is_checked=True)
    serializer_class = HostingSerializer

    def list(self, request, *args, **kwargs):
        hosting = self.queryset.all()
        serializer = HostingReadableSerializer(hosting, many=True)
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
