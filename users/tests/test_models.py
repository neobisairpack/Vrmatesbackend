from django.test import TestCase

from users.models import MyUser, Rating


class UserTest(TestCase):
    def setUp(self):
        self.user = MyUser.objects.create_user(
            'Scareface', 'admin@mail.ru'
        )

    def test_user_email(self):
        self.assertEqual(self.user.email, 'admin@mail.ru')

    def test_user_username(self):
        self.assertEqual(self.user.username, 'Scareface')


class RatingTest(TestCase):
    def setUp(self):
        self.user = MyUser.objects.create_user(
            'Scareface', 'admin@mail.ru'
        )
        self.rating = Rating.objects.create(
            user=self.user, rating=3.5
        )

    def test_rating_user(self):
        self.assertEqual(self.rating.user.username, 'Scareface')

    def test_rating_rating(self):
        self.assertEqual(self.rating.rating, 3.5)
