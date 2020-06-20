from django.test import TestCase
from datetime import datetime, date

from users.models import User
from services.models import Service, Hosting


class ServiceModelTest(TestCase):
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
        Service.objects.create(
            requester=user1,
            provider=user1,
            service_type='Package delivery',
            start_location='Start',
            end_location='End',
            deadline=datetime.now(),
            status='Canceled',
            title='Title',
            text='Text',
            is_checked=False
        )

    service = Service.objects.get(id=1)

    def test_requester_field(self):
        field_label = self.service._meta.get_field('requester').verbose_name
        self.assertEqual(field_label, 'requester')

    def test_provider_field(self):
        field_label = self.service._meta.get_field('provider').verbose_name
        self.assertEqual(field_label, 'provider')

    def test_service_type_field(self):
        field_label = self.service._meta.get_field('service_type').verbose_name
        field_max_length = self.service._meta.get_field('service_type').max_length
        self.assertEqual(field_label, 'service type')
        self.assertEqual(field_max_length, 32)

    def test_start_location_field(self):
        field_label = self.service._meta.get_field('start_location').verbose_name
        field_max_length = self.service._meta.get_field('start_location').max_length
        self.assertEqual(field_label, 'start location')
        self.assertEqual(field_max_length, 128)

    def test_end_location_field(self):
        field_label = self.service._meta.get_field('end_location').verbose_name
        field_max_length = self.service._meta.get_field('end_location').max_length
        self.assertEqual(field_label, 'end location')
        self.assertEqual(field_max_length, 128)

    def test_deadline_field(self):
        field_label = self.service._meta.get_field('deadline').verbose_name
        self.assertEqual(field_label, 'deadline')

    def test_status_field(self):
        field_label = self.service._meta.get_field('status').verbose_name
        field_max_length = self.service._meta.get_field('status').max_length
        field_default = self.service._meta.get_field('status').default
        self.assertEqual(field_label, 'status')
        self.assertEqual(field_max_length, 64)
        self.assertEqual(field_default, 'Created, not accepted')

    def test_title_field(self):
        field_label = self.service._meta.get_field('title').verbose_name
        field_max_length = self.service._meta.get_field('title').max_length
        self.assertEqual(field_label, 'title')
        self.assertEqual(field_max_length, 128)

    def test_text_field(self):
        field_label = self.service._meta.get_field('text').verbose_name
        field_max_length = self.service._meta.get_field('text').max_length
        self.assertEqual(field_label, 'text')
        self.assertEqual(field_max_length, 512)

    def test_is_checked_field(self):
        field_label = self.service._meta.get_field('is_checked').verbose_name
        field_default = self.service._meta.get_field('is_checked').default
        self.assertEqual(field_label, 'is checked')
        self.assertEqual(field_default, False)


class HostingModelTest(TestCase):
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
        Hosting.objects.create(
            requester=user1,
            provider=user1,
            service_type='Hosting',
            title='Title',
            text='Text',
            date=date.today(),
            preferences='Living room',
            status='Canceled',
            is_checked=False
        )

    hosting = Hosting.objects.get(id=2)

    def test_requester_field(self):
        field_label = self.hosting._meta.get_field('requester').verbose_name
        self.assertEqual(field_label, 'requester')

    def test_provider_field(self):
        field_label = self.hosting._meta.get_field('provider').verbose_name
        self.assertEqual(field_label, 'provider')

    def test_service_type_field(self):
        field_label = self.hosting._meta.get_field('service_type').verbose_name
        field_max_length = self.hosting._meta.get_field('service_type').max_length
        self.assertEqual(field_label, 'service type')
        self.assertEqual(field_max_length, 32)

    def test_title_field(self):
        field_label = self.hosting._meta.get_field('title').verbose_name
        field_max_length = self.hosting._meta.get_field('title').max_length
        self.assertEqual(field_label, 'title')
        self.assertEqual(field_max_length, 128)

    def test_text_field(self):
        field_label = self.hosting._meta.get_field('text').verbose_name
        field_max_length = self.hosting._meta.get_field('text').max_length
        self.assertEqual(field_label, 'text')
        self.assertEqual(field_max_length, 512)

    def test_date_field(self):
        field_label = self.hosting._meta.get_field('date').verbose_name
        self.assertEqual(field_label, 'date')

    def test_preferences_field(self):
        field_label = self.hosting._meta.get_field('preferences').verbose_name
        field_max_length = self.hosting._meta.get_field('preferences').max_length
        self.assertEqual(field_label, 'preferences')
        self.assertEqual(field_max_length, 64)

    def test_status_field(self):
        field_label = self.hosting._meta.get_field('status').verbose_name
        field_max_length = self.hosting._meta.get_field('status').max_length
        field_default = self.hosting._meta.get_field('status').default
        self.assertEqual(field_label, 'status')
        self.assertEqual(field_max_length, 64)
        self.assertEqual(field_default, 'Created, not accepted')

    def test_is_checked_field(self):
        field_label = self.hosting._meta.get_field('is_checked').verbose_name
        field_default = self.hosting._meta.get_field('is_checked').default
        self.assertEqual(field_label, 'is checked')
        self.assertEqual(field_default, False)
