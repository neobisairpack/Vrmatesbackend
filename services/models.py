import datetime
from django.db import models
from django.dispatch import receiver
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.db.models.signals import post_save


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
        if self.requester and self.requester.points < 20:
            if self.is_checked:
                super(Service, self).save(*args, **kwargs)
            return "Not enough points"
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
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS, max_length=64, default='Pending')
    accept = models.BooleanField(default=False)

    def __str__(self):
        return '%s' % self.service


@receiver(post_save, sender=RequestService)
def service_status(sender, instance, created, **kwargs):
    if instance.status == 'Accepted' or instance.accept:
        status = 'Accepted/in process'
        service = instance.service
        service.status = status
        service.provider = instance.requester
        service.save()


@receiver(post_save, sender=Service)
def pull_service_points(sender, instance, created, **kwargs):
    if created and instance.requester:
        points = 20
        user = instance.requester
        user_points = user.points
        user_points -= points
        user.points = user_points
        user.created_posts += 1
        user.save()


@receiver(post_save, sender=Service)
def pay_service_points(sender, instance, created, **kwargs):
    if instance.status == "Successfully done":
        if instance.provider is not None:
            points = 20
            user = instance.provider
            user.points += points
            user.save()
        if instance.provider is None:
            points = 20
            user = instance.requester
            user.points += points
            user.save()


@receiver(post_save, sender=Service)
def service_cancel_points(sender, instance, created, **kwargs):
    deadline = instance.deadline
    today = datetime.datetime.now().date()
    timer = deadline - today

    if instance.status == 'Canceled' and instance.provider is None:
        instance.requester.points += 20
        instance.requester.save()

    if instance.status == 'Canceled' and timer.days > 2:
        if instance.provider is not None:
            instance.requester.points += 10
            instance.provider.points += 10
            instance.requester.save()
            instance.provider.save()
        if instance.provider is None:
            instance.requester.points += 20
            instance.requester.save()

    if instance.status == 'Canceled' and timer.days < 2:
        if instance.provider is not None:
            instance.provider.points += 20
            instance.provider.save()
        if instance.provider is None:
            instance.requester.points += 20
            instance.requester.save()


@receiver(post_save, sender=Service)
def service_expired(sender, instance, created, **kwargs):
    deadline = instance.deadline
    today = datetime.datetime.now().date()
    timer = deadline - today
    if timer.days < 0:
        service = instance
        service.status = 'Expired'
        service.save()


@receiver(post_save, sender=Service)
def service_cancel_notification(sender, instance, created, **kwargs):
    if instance.status == 'Canceled':
        if instance.requester is not None:
            mail_subject = 'Status changed | Vrmates team'
            message = render_to_string('services/service_canceled.html', {
                'user': instance.requester.first_name,
                'title': instance.title,
                'status': instance.status
            })
            to_email = instance.requester.email
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
        if instance.provider is not None:
            mail_subject = 'Status changed | Vrmates team'
            message = render_to_string('services/service_canceled.html', {
                'user': instance.requester.first_name,
                'title': instance.title,
                'status': instance.status
            })
            to_email = instance.provider.email
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()


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
    service = models.ForeignKey(ProvideService, on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS, max_length=64, default='Pending')
    accept = models.BooleanField(default=False)

    def __str__(self):
        return str(self.service)


@receiver(post_save, sender=RequestProvideService)
def provide_service_status(sender, instance, created, **kwargs):
    if instance.status == 'Accepted' or instance.accept:
        status = 'Accepted/in process'
        service = instance.service
        service.status = status
        service.requester = instance.requester
        service.save()


@receiver(post_save, sender=ProvideService)
def pull_service_provide_points(sender, instance, created, **kwargs):
    if created and instance.status == 'Accepted/in process' and instance.requester:
        points = 20
        user = instance.requester
        user_points = user.points
        user_points -= points
        user.points = user_points
        user.save()


@receiver(post_save, sender=ProvideService)
def pay_service_provide_points(sender, instance, created, **kwargs):
    if instance.status == "Successfully done":
        points = 20
        user = instance.provider
        user_points = user.points
        user_points += points
        user.points = user_points
        user.save()


@receiver(post_save, sender=ProvideService)
def service_cancel_points(sender, instance, created, **kwargs):
    deadline = instance.deadline
    today = datetime.datetime.now().date()
    timer = deadline - today

    if instance.status == 'Canceled' and instance.provider is None:
        instance.requester.points += 20
        instance.requester.save()

    if instance.status == 'Canceled' and timer.days > 2:
        if instance.requester is not None:
            instance.provider.points += 10
            instance.requester.points += 10
            instance.provider.save()
            instance.requester.save()
        if instance.requester is None:
            instance.provider.points += 20
            instance.provider.save()

    if instance.status == 'Canceled' and timer.days < 2:
        if instance.requester is not None:
            instance.requester.points += 20
            instance.requester.save()
        if instance.requester is None:
            instance.provider.points += 20
            instance.provider.save()


@receiver(post_save, sender=ProvideService)
def service_expired(sender, instance, created, **kwargs):
    deadline = instance.deadline
    today = datetime.datetime.now().date()
    timer = deadline - today
    if timer.days < 0:
        service = instance
        service.status = 'Expired'
        service.save()


@receiver(post_save, sender=ProvideService)
def provide_service_cancel_notification(sender, instance, created, **kwargs):
    if instance.status == 'Canceled':
        if instance.requester is not None:
            mail_subject = 'Status changed | Vrmates team'
            message = render_to_string('services/service_canceled.html', {
                'user': instance.requester.first_name,
                'title': instance.title,
                'status': instance.status
            })
            to_email = instance.requester.email
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
        if instance.provider is not None:
            mail_subject = 'Status changed | Vrmates team'
            message = render_to_string('services/service_canceled.html', {
                'user': instance.requester.first_name,
                'title': instance.title,
                'status': instance.status
            })
            to_email = instance.provider.email
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
