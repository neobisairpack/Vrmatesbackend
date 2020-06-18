from django.urls import include, path
from rest_framework import routers

from .views import ServiceViewSet, HostingViewSet


router = routers.DefaultRouter()
router.register('service', ServiceViewSet)
router.register('hosting', HostingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
