from django.db import models
from django.dispatch import receiver
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.db.models.signals import post_save


class Service(models.Model):
    SERVICE_TYPE = (
        ('Package delivery', 'Package delivery'),
        ('Airport pick up/drop off', 'Airport pick up/drop off'),
    )
    STATUS = (
        ('Created, not accepted', 'Created, not accepted'),
        ('Accepted/in process', 'Accepted/in process'),
        ('Successfully done', 'Successfully done'),
        ('Not confirmed', 'Not confirmed'),
        ('Canceled', 'Canceled')
    )
    requester = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='user_requester')
    provider = models.ForeignKey('users.User', on_delete=models.CASCADE,
                                 related_name='user_provider', null=True, blank=True)
    service_type = models.CharField(choices=SERVICE_TYPE, max_length=32)
    start_location = models.CharField(max_length=128)
    end_location = models.CharField(max_length=128)
    deadline = models.DateTimeField()
    status = models.CharField(choices=STATUS, max_length=64, default='Created, not accepted')
    title = models.CharField(max_length=128)
    text = models.TextField(max_length=512)
    image = models.ImageField(null=True, blank=True)
    is_checked = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.requester.points < 20:
            if self.is_checked:
                super(Service, self).save(*args, **kwargs)
            return "Not enough points"
        elif self.is_checked:
            super(Service, self).save(*args, **kwargs)


@receiver(post_save, sender=Service)
def pull_service_points(sender, instance, created, **kwargs):
    if created:
        points = 20
        user = instance.requester
        user_points = user.points
        user_points -= points
        user.points = user_points
        user.save()


@receiver(post_save, sender=Service)
def pay_service_points(sender, instance, created, **kwargs):
    if instance.status == "Successfully done":
        points = 20
        user = instance.provider
        user_points = user.points
        user_points += points
        user.points = user_points
        user.save()


class Hosting(models.Model):
    SERVICE_TYPE = (
        ('Hosting', 'Hosting'),
    )
    PREFS = (
        ('Private bedroom', 'Private bedroom'),
        ('Living room', 'Living room'),
        ('Common space', 'Common space')
    )
    STATUS = (
        ('Created, not accepted', 'Created, not accepted'),
        ('Accepted/in process', 'Accepted/in process'),
        ('Successfully done', 'Successfully done'),
        ('Not confirmed', 'Not confirmed'),
        ('Canceled', 'Canceled')
    )
    requester = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='hosting_requester')
    provider = models.ForeignKey('users.User', on_delete=models.CASCADE,
                                 related_name='hosting_provider', null=True, blank=True)
    date = models.DateField()
    service_type = models.CharField(choices=SERVICE_TYPE, max_length=32, default='Hosting')
    title = models.CharField(max_length=128)
    text = models.TextField(max_length=512)
    preferences = models.CharField(max_length=64, choices=PREFS)
    status = models.CharField(max_length=64, choices=STATUS, default='Created, not accepted')
    image = models.ImageField(null=True, blank=True)
    is_checked = models.BooleanField(default=False)


@receiver(post_save, sender=Hosting)
def pull_hosting_points(sender, instance, created, **kwargs):
    if created:
        points = 20
        user = instance.requester
        user_points = user.points
        user_points -= points
        user.points = user_points
        user.save()


@receiver(post_save, sender=Hosting)
def pay_hosting_points(sender, instance, created, **kwargs):
    if instance.status == "Successfully done":
        points = 20
        user = instance.provider
        user_points = user.points
        user_points += points
        user.points = user_points
        user.save()


@receiver(post_save, sender=Service)
def service_cancel_notification(sender, instance, created, **kwargs):
    if instance.status == 'Canceled':
        mail_subject = 'Status changed | Vrmates team'
        message = render_to_string('services/service_canceled.html', {
                'user': instance.requester.first_name,
                'provider': instance.provider.first_name,
                'title': instance.title,
                'status': instance.status
            })
        to_email = instance.requester.email
        email = EmailMessage(
            mail_subject, message, to=[to_email]
        )
        email.send()


@receiver(post_save, sender=Hosting)
def service_cancel_notification(sender, instance, created, **kwargs):
    if instance.status == 'Canceled':
        mail_subject = 'Status changed | Vrmates team'
        message = render_to_string('services/service_canceled.html', {
            'user': instance.requester.first_name,
            'provider': instance.provider.first_name,
            'title': instance.title,
            'status': instance.status
        })
        to_email = instance.requester.email
        email = EmailMessage(
            mail_subject, message, to=[to_email]
        )
        email.send()
