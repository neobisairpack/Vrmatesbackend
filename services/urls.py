from django.urls import include, path
from rest_framework import routers

from .views import *
from users.views import RatingViewSet


router = routers.DefaultRouter()
router.register('services', ServiceViewSet)
router.register('services-images', ServiceImageViewSet)
router.register('request-services', RequestServiceViewSet)
router.register('provide-services', ProvideServiceViewSet)
router.register('provide-services-images', ProvideServiceImageViewSet)
router.register('request-provide-services', RequestProvideServiceViewSet)
router.register('rating', RatingViewSet)
router.register('support', SupportViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('service-filters/', ServiceFilterListAPIView.as_view()),
    path('support-filters/', SupportFilterListAPIView.as_view()),
]
