from django.urls import reverse
from rest_framework import status
from rest_framework.test import (
    APITestCase,
    APIClient,
    APIRequestFactory,
)

from users.models import User

factory = APIRequestFactory()


class GetUserTest(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='Scareface', email='admin@mail.ru', birthday='1998-11-10', password='Admin123'
        )
        self.client.login(username='Scareface', password='Admin123')

    def test_user_retrieve(self):
        self.client.login(username='Scareface', password='Admin123')
        response = self.client.get(reverse('users:users'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
