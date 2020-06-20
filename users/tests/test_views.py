import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from users.models import User


class UserTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(
            username='Scareface',
            email='tektonik_boy98@mail.ru',
            password='Admin12345'
        )

    user = User.objects.get(username='Scareface')
    client = APIClient()
    client.force_authenticate(user=user)

    def test_registration(self):
        self.client.login(username='Scareface', password='Admin12345')
        url = reverse('users:registration')
        data = {
            "first_name": "Alex",
            "last_name": "Chirkov",
            "username": "Scareface",
            "email": "aleksei.chirkov.98@gmail.com",
            "birthday": "2020-12-24",
            "gender": "Male",
            "phone": "996559129557",
            "address": "Moscow st. 219",
            "zip_code": 720010,
            "country": "Kyrgyzstan",
            "city": "Bishkek",
            "state": "Chui",
            "password": "MyPassword1",
            "password2": "MyPassword1"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'Scareface')

    def test_login(self):
        self.client.login(email='tektinik_boy98@mail.ru', password='Admin12345')
        url = reverse('users:login')
        data = {
            'email': 'tektonik_boy98@mail.ru',
            'password': 'Admin12345'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
