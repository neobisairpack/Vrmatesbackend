from django.urls import path
from django.conf.urls import url

from .views import (
    RegistrationAPIView,
    LoginAPIView,
    UserRetrieveUpdateAPIView,
    activate
)


app_name = 'users'

urlpatterns = [
    path('users/', UserRetrieveUpdateAPIView.as_view(), name='users'),
    path('users/registration/', RegistrationAPIView.as_view()),
    path('users/login/', LoginAPIView.as_view()),
    url(r'activate/(?P<uid64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        activate, name='activate'),
]
