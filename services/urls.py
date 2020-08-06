from django.urls import include, path
from rest_framework import routers

from .views import *
from users.views import RatingViewSet


router = routers.DefaultRouter()
router.register('delivery', DeliveryViewSet)
router.register('delivery-images', DeliveryImageViewSet)
router.register('request-delivery', RequestDeliveryViewSet)
router.register('pickup', PickUpViewSet)
router.register('pickup-images', DeliveryImageViewSet)
router.register('request-pickup', RequestPickUpViewSet)
router.register('hosting', HostingViewSet)
router.register('hosting-images', DeliveryImageViewSet)
router.register('request-hosting', RequestHostingViewSet)
router.register('provide-delivery', ProvideDeliveryViewSet)
router.register('request-provide-delivery', RequestProvideDeliveryViewSet)
router.register('provide-pickup', ProvidePickUpViewSet)
router.register('request-provide-pickup', RequestProvidePickUpViewSet)
router.register('provide-hosting', ProvideHostingViewSet)
router.register('request-provide-hosting', RequestProvideHostingViewSet)
router.register('rating', RatingViewSet)
router.register('support', SupportViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('pickup-filters/', PickUpFilterListAPIView.as_view()),
    path('delivery-filters/', DeliveryFilterListAPIView.as_view()),
    path('hosting-filters/', HostingFilterListAPIView.as_view()),
    path('support-filters/', SupportFilterListAPIView.as_view()),
]
