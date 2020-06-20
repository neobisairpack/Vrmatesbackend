from django.test import TestCase

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
        field_unique = self.user._meta.get_field('username').unique
        self.assertEqual(field_label, 'username')
        self.assertEqual(field_max_length, 64)
        self.assertEqual(field_unique, True)

    def test_email_field(self):
        field_label = self.user._meta.get_field('email').verbose_name
        field_unique = self.user._meta.get_field('email').unique
        self.assertEqual(field_label, 'email')
        self.assertEqual(field_unique, True)

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
        field_unique = self.user._meta.get_field('phone').unique
        self.assertEqual(field_label, 'phone')
        self.assertEqual(field_max_length, 64)
        self.assertEqual(field_unique, True)

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
        field_default = self.user._meta.get_field('points').default
        self.assertEqual(field_label, 'points')
        self.assertEqual(field_default, 20)


class RatingModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user1 = User.objects.create(
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
        )
        user2 = User.objects.create(
            first_name='Zhenya',
            last_name='Kiselyov',
            email='test@mail.ru',
            username='Zhenwina',
            birthday='1998-11-10',
            gender='Male',
            phone='12345678',
            country='country',
            zip_code='zip',
            state='state',
            city='city',
            address='address',
            points=20,
        )
        Rating.objects.create(
            requester=user1,
            provider=user2,
            rating=4.4,
            text='Good job',
            date='2020-06-20'
        )

    rating = Rating.objects.get(id=1)

    def test_requester_field(self):
        field_label = self.rating._meta.get_field('requester').verbose_name
        self.assertEqual(field_label, 'requester')

    def test_provider_field(self):
        field_label = self.rating._meta.get_field('provider').verbose_name
        self.assertEqual(field_label, 'provider')

    def test_rating_field(self):
        field_label = self.rating._meta.get_field('rating').verbose_name
        self.assertEqual(field_label, 'rating')

    def test_text_field(self):
        field_label = self.rating._meta.get_field('text').verbose_name
        field_max_length = self.rating._meta.get_field('text').max_length
        self.assertEqual(field_label, 'text')
        self.assertEqual(field_max_length, 512)

    def test_date_field(self):
        field_label = self.rating._meta.get_field('date').verbose_name
        field_auto_now_add = self.rating._meta.get_field('date').auto_now_add
        self.assertEqual(field_label, 'date')
        self.assertEqual(field_auto_now_add, True)

