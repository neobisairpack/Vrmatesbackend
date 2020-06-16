from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from users.models import User
from users.serializers import UserSerializer


class UserSerializerTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='Scareface', email='admin@mail.ru', birthday='1998-11-10', password='Admin123'
        )
        self.client.login(username='Scareface', password='Admin123')

    def test_user_serializer(self):
        self.client.login(username='Scareface', password='Admin123')
        response = self.client.get(reverse('users:users'))
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        self.assertEqual(response.data, serializer.data)
