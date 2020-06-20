from django.test import TestCase
from django.core.files import File

from users.models import User, Rating


class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create(
            first_name='Alex',
            last_name='Chirkov',
            email='admin@mail.ru',
            username='Scareface',
            birthday='1998-11-10',
            gender='Male',
            phone='12345',
            country='country',
            zip_code='zip',
            state='state',
            city='city',
            address='address',
            points=20,
            # avg_rating=3.4,
            # rating_count=3,
            # avg_rating_last_ten=3.4,
            # canceled_posts_count=2
        )

    user = User.objects.get(id=1)

    def test_user_name_is_first_name_and_last_name(self):
        expected_user_name = f'{self.user.first_name} {self.user.last_name}'
        self.assertEqual(expected_user_name, str(self.user))

    def test_first_name_field(self):
        field_label = self.user._meta.get_field('first_name').verbose_name
        field_max_length = self.user._meta.get_field('first_name').max_length
        self.assertEqual(field_label, 'first name')
        self.assertEqual(field_max_length, 64)

    def test_last_name_field(self):
        field_label = self.user._meta.get_field('last_name').verbose_name
        field_max_length = self.user._meta.get_field('last_name').max_length
        self.assertEqual(field_label, 'last name')
        self.assertEqual(field_max_length, 64)

    def test_username_field(self):
        field_label = self.user._meta.get_field('username').verbose_name
        field_max_length = self.user._meta.get_field('username').max_length
        self.assertEqual(field_label, 'username')
        self.assertEqual(field_max_length, 64)

    def test_email_field(self):
        field_label = self.user._meta.get_field('email').verbose_name
        self.assertEqual(field_label, 'email')

    def test_birthday_field(self):
        field_label = self.user._meta.get_field('birthday').verbose_name
        self.assertEqual(field_label, 'birthday')

    def test_gender_field(self):
        field_label = self.user._meta.get_field('gender').verbose_name
        field_max_length = self.user._meta.get_field('gender').max_length
        self.assertEqual(field_label, 'gender')
        self.assertEqual(field_max_length, 16)

    def test_phone_field(self):
        field_label = self.user._meta.get_field('phone').verbose_name
        field_max_length = self.user._meta.get_field('phone').max_length
        self.assertEqual(field_label, 'phone')
        self.assertEqual(field_max_length, 64)

    def test_country_field(self):
        field_label = self.user._meta.get_field('country').verbose_name
        field_max_length = self.user._meta.get_field('country').max_length
        self.assertEqual(field_label, 'country')
        self.assertEqual(field_max_length, 128)

    def test_zip_code_field(self):
        field_label = self.user._meta.get_field('zip_code').verbose_name
        field_max_length = self.user._meta.get_field('zip_code').max_length
        self.assertEqual(field_label, 'zip code')
        self.assertEqual(field_max_length, 32)

    def test_state_field(self):
        field_label = self.user._meta.get_field('state').verbose_name
        field_max_length = self.user._meta.get_field('state').max_length
        self.assertEqual(field_label, 'state')
        self.assertEqual(field_max_length, 128)

    def test_city_filed(self):
        field_label = self.user._meta.get_field('city').verbose_name
        field_max_length = self.user._meta.get_field('city').max_length
        self.assertEqual(field_label, 'city')
        self.assertEqual(field_max_length, 128)

    def test_address_label(self):
        field_label = self.user._meta.get_field('address').verbose_name
        field_max_length = self.user._meta.get_field('address').max_length
        self.assertEqual(field_label, 'address')
        self.assertEqual(field_max_length, 128)

    def test_points_label(self):
        field_label = self.user._meta.get_field('points').verbose_name
        self.assertEqual(field_label, 'points')
