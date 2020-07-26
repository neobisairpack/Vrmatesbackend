from django.urls import include, path
from rest_framework import routers

from .views import *
from users.views import RatingViewSet


router = routers.DefaultRouter()
router.register('service', ServiceViewSet)
router.register('hosting', HostingViewSet)
router.register('rating', RatingViewSet)
router.register('support', SupportViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('service-filters/', ServiceFilterListAPIView.as_view()),
    path('hosting-filters/', HostingFilterListAPIView.as_view()),
    path('support-filters/', SupportFilterListAPIView.as_view()),
]
