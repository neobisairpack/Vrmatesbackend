from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.validators import MaxValueValidator, MinValueValidator

from users.models import MyUser, Rating


class PackageDelivery(models.Model):
    SERVICE_TYPE = (
        ('Package delivery', 'Package delivery'),
        ('Airport pick up/drop off', 'Airport pick up/drop off'),
        ('Hosting', 'Hosting'),
    )
    STATUS = (
        ('Created, not accepted', 'Created, not accepted'),
        ('Accepted/in process', 'Accepted/in process'),
        ('Successfully done', 'Successfully done'),
        ('Not confirmed', 'Not confirmed'),
        ('Canceled', 'Canceled')
    )
    requester = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='user_requester')
    provider = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='user_provider')
    service_type = models.CharField(choices=SERVICE_TYPE, max_length=32)
    start_location = models.CharField(max_length=128)
    end_location = models.CharField(max_length=128)
    deadline = models.DateTimeField()
    status = models.CharField(choices=STATUS, max_length=64)
    title = models.CharField(max_length=128)
    text = models.TextField(max_length=512)
    image = models.ImageField()
    rating = models.FloatField(validators=[MinValueValidator(1.0), MaxValueValidator(5.0)])
