from django.urls import include, path
from rest_framework import routers

from .views import *
from users.views import RatingViewSet


router = routers.DefaultRouter()
router.register('delivery', DeliveryViewSet)
router.register('request-delivery', RequestDeliveryViewSet)
router.register('pickup', PickUpViewSet)
router.register('request-delivery', RequestPickUpViewSet)
router.register('hosting', HostingViewSet)
router.register('request-delivery', RequestHostingViewSet)
router.register('delivery', ProvideDeliveryViewSet)
router.register('pickup', ProvidePickUpViewSet)
router.register('hosting', ProvideHostingViewSet)
router.register('rating', RatingViewSet)
router.register('support', SupportViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('pickup-filters/', PickUpFilterListAPIView.as_view()),
    path('delivery-filters/', DeliveryFilterListAPIView.as_view()),
    path('hosting-filters/', HostingFilterListAPIView.as_view()),
    path('support-filters/', SupportFilterListAPIView.as_view()),
]
