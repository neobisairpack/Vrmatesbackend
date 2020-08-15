from django.urls import include, path
from rest_framework import routers

from .views import *
from users.views import RatingViewSet


router = routers.DefaultRouter()
router.register('service', ServiceViewSet)
router.register('service-images', ServiceImageViewSet)
router.register('request-service', RequestServiceViewSet)
router.register('provide-service', ProvideServiceViewSet)
router.register('request-provide-service', RequestProvideServiceViewSet)
router.register('rating', RatingViewSet)
router.register('support', SupportViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('service-filters/', ServiceFilterListAPIView.as_view()),
    path('support-filters/', SupportFilterListAPIView.as_view()),
]
