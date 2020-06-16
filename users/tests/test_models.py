from django.test import TestCase

from users.models import User, Rating


class UserTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='Scareface', email='admin@mail.ru', birthday='1998-11-10'
        )

    def test_user_username(self):
        self.assertEqual(self.user.username, 'Scareface')

    def test_user_email(self):
        self.assertEqual(self.user.email, 'admin@mail.ru')


class RatingTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='Scareface', email='admin@mail.ru', birthday='1998-11-10', password='Admin123'
        )
        self.rating = Rating.objects.create(
            user=self.user, rating=3.5
        )

    def test_rating_user(self):
        self.assertEqual(self.rating.user.username, 'Scareface')

    def test_rating_rating(self):
        self.assertEqual(self.rating.rating, 3.5)
