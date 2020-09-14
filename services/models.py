import datetime
from django.db import models
from django.db.models import UniqueConstraint


class Service(models.Model):
    STATUS = (
        ('Created, not accepted', 'Created, not accepted'),
        ('Accepted/in process', 'Accepted/in process'),
        ('Successfully done', 'Successfully done'),
        ('Not confirmed', 'Not confirmed'),
        ('Expired', 'Expired'),
        ('Canceled', 'Canceled')
    )
    TYPE = (
        ('Delivery', 'Delivery'),
        ('Pick Up', 'Pick Up'),
        ('Hosting', 'Hosting'),
    )
    PREFS = (
        ('Private bedroom', 'Private bedroom'),
        ('Living room', 'Living room'),
        ('Common space', 'Common space'),
    )
    requester = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='requester',
                                  blank=True, null=True)
    provider = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='provider',
                                 blank=True, null=True)
    requester_from = models.CharField(max_length=128, blank=True, null=True)
    service_type = models.CharField(max_length=128, choices=TYPE, blank=True, null=True)
    country = models.CharField(max_length=128, blank=True, null=True)
    preferences = models.CharField(max_length=128, choices=PREFS, blank=True, null=True)
    pickup_location = models.CharField(max_length=128, blank=True, null=True)
    drop_off_location = models.CharField(max_length=128, blank=True, null=True)
    arrive_date = models.DateTimeField(blank=True, null=True)
    deadline = models.DateField()
    status = models.CharField(choices=STATUS, max_length=64, default='Created, not accepted',
                              blank=True, null=True)
    title = models.CharField(max_length=128, blank=True, null=True)
    text = models.TextField(max_length=512, null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    is_checked = models.BooleanField(default=False)

    def __str__(self):
        return str(self.title)

    def save(self, *args, **kwargs):
        deadline = self.deadline
        today = datetime.datetime.now().date()
        if deadline < today:
            self.status = 'Expired'
            super(Service, self).save(*args, **kwargs)
        if self.is_checked:
            super(Service, self).save(*args, **kwargs)
        elif self.requester and self.requester.points < 20:
            raise TypeError('Not enough points.')
        else:
            super(Service, self).save(*args, **kwargs)


class ServiceImage(models.Model):
    post = models.ForeignKey(Service, default=None, on_delete=models.CASCADE,
                             blank=True, null=True, related_name='images')
    image = models.ImageField(upload_to='services_images')

    def __str__(self):
        return str(self.post)


class RequestService(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Canceled', 'Canceled'),
    )
    requester = models.ForeignKey('users.User', on_delete=models.CASCADE, blank=True, null=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, blank=True, null=True)
    status = models.CharField(choices=STATUS, max_length=64, default='Pending')
    accept = models.BooleanField(default=False)

    class Meta:
        constraints = [UniqueConstraint(fields=['requester', 'service'], name='unique_request_service')]

    def __str__(self):
        return '%s' % self.service


class Support(models.Model):
    email = models.EmailField(unique=False)
    title = models.CharField(max_length=128)
    text = models.TextField(max_length=512)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return '%s' % self.title


class ProvideService(models.Model):
    STATUS = (
        ('Created, not accepted', 'Created, not accepted'),
        ('Accepted/in process', 'Accepted/in process'),
        ('Successfully done', 'Successfully done'),
        ('Not confirmed', 'Not confirmed'),
        ('Expired', 'Expired'),
        ('Canceled', 'Canceled')
    )
    TYPE = (
        ('Delivery', 'Delivery'),
        ('Pick Up', 'Pick Up'),
        ('Hosting', 'Hosting'),
    )
    PREFS = (
        ('Private bedroom', 'Private bedroom'),
        ('Living room', 'Living room'),
        ('Common space', 'Common space'),
    )
    provider = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='provide_service_user',
                                 null=True, blank=True)
    requester = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='provider_service_requester',
                                  blank=True, null=True)
    provider_from = models.CharField(max_length=128, blank=True, null=True)
    service_type = models.CharField(max_length=128, choices=TYPE, blank=True, null=True)
    country = models.CharField(max_length=128, blank=True, null=True)
    preferences = models.CharField(max_length=128, choices=PREFS, blank=True, null=True)
    pickup_location = models.CharField(max_length=128, blank=True, null=True)
    drop_off_location = models.CharField(max_length=128, blank=True, null=True)
    arrive_date = models.DateTimeField(blank=True, null=True)
    deadline = models.DateField()
    title = models.CharField(max_length=64, blank=True, null=True)
    text = models.TextField(max_length=640, null=True, blank=True)
    status = models.CharField(choices=STATUS, max_length=64, blank=True, null=True, default='Created, not accepted')
    created = models.DateField(auto_now_add=True)
    is_checked = models.BooleanField(default=False)

    def __str__(self):
        return str(self.title)

    def save(self, *args, **kwargs):
        deadline = self.deadline
        today = datetime.datetime.now().date()
        if deadline < today:
            self.status = 'Expired'
            super(ProvideService, self).save(*args, **kwargs)
        else:
            super(ProvideService, self).save(*args, **kwargs)


class ProvideServiceImage(models.Model):
    post = models.ForeignKey(ProvideService, default=None, on_delete=models.CASCADE,
                             blank=True, null=True, related_name='images')
    image = models.ImageField(upload_to='provide_services_images')

    def __str__(self):
        return str(self.post)


class RequestProvideService(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Canceled', 'Canceled'),
    )
    requester = models.ForeignKey('users.User', on_delete=models.CASCADE, blank=True, null=True)
    service = models.OneToOneField(ProvideService, on_delete=models.CASCADE, related_name='request')
    status = models.CharField(choices=STATUS, max_length=64, default='Pending')
    accept = models.BooleanField(default=False)

    class Meta:
        constraints = [UniqueConstraint(fields=['requester', 'service'], name='unique_request_provide_services')]

    def __str__(self):
        return str(self.service)


class UsersWorkInService(models.Model):
    """Модель показывает, кем является юзер в конкретном запросе на услугу"""

    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    service = models.ForeignKey('services.Service', on_delete=models.CASCADE, related_name='workers')

    is_provider = models.BooleanField(default=False)
    is_requester = models.BooleanField(default=False)

    class Meta:
        unique_together = ['user', 'service']


def is_provider(user, service) -> bool:
    """check if user provider"""
    try:
        work = UsersWorkInService.objects.get(user=user, service=service)
        return work.is_provider
    except UsersWorkInService.DoesNotExist:
        raise TypeError('Provider does not exist.')


def is_requester(user, service) -> bool:
    """check if user requester"""
    try:
        work = UsersWorkInService.objects.get(user=user, service=service)
        return work.is_requester
    except UsersWorkInService.DoesNotExist:
        raise TypeError('Requester does not exist.')
