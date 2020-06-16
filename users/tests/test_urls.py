from django.urls import resolve
from django.test import TestCase

from users.views import (
    RegistrationAPIView,
    LoginAPIView,
    UserRetrieveUpdateAPIView,
    RatingAPIView
)


class URLTest(TestCase):
    def test_registration_url(self):
        resolver = resolve('/api/users/registration/')
        self.assertEqual(resolver.func.cls, RegistrationAPIView)

    def test_login_url(self):
        resolver = resolve('/api/users/login/')
        self.assertEqual(resolver.func.cls, LoginAPIView)

    def test_user_url(self):
        resolver = resolve('/api/users/')
        self.assertEqual(resolver.func.cls, UserRetrieveUpdateAPIView)

    def test_rating_url(self):
        resolver = resolve('/api/users/rating/')
        self.assertEqual(resolver.func.cls, RatingAPIView)
