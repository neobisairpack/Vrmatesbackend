from django.urls import include, path
from rest_framework import routers

from .views import ServiceViewSet, HostingViewSet
from users.views import RatingViewSet


router = routers.DefaultRouter()
router.register('service', ServiceViewSet)
router.register('hosting', HostingViewSet)
router.register('rating', RatingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
