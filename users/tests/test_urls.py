from django.urls import path, reverse
from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase

from users.views import (
    RegistrationAPIView,
)


class UsersTest(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path('users/registration', RegistrationAPIView.as_view(), name='users'),
    ]

    def test_registration_url(self):
        url = reverse('users')
        response = self.client.post(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 13)
