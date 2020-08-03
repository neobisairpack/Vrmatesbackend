from django.db import models
from django.dispatch import receiver
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.db.models.signals import post_save


# class Service(models.Model):
#     STATUS = (
#         ('Created, not accepted', 'Created, not accepted'),
#         ('Accepted/in process', 'Accepted/in process'),
#         ('Successfully done', 'Successfully done'),
#         ('Not confirmed', 'Not confirmed'),
#         ('Canceled', 'Canceled')
#     )
#     requester = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='service_requester')
#     provider = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='service_provider',
#                                  blank=True, null=True)
#     status = models.CharField(choices=STATUS, max_length=64, default='Created, not accepted')
#     title = models.CharField(max_length=128)
#     text = models.TextField(max_length=640)
#     image = models.ImageField(upload_to='services', null=True, blank=True)
#     created = models.DateField(auto_now_add=True)
#     is_checked = models.BooleanField(default=False)


class Delivery(models.Model):
    STATUS = (
        ('Created, not accepted', 'Created, not accepted'),
        ('Accepted/in process', 'Accepted/in process'),
        ('Successfully done', 'Successfully done'),
        ('Not confirmed', 'Not confirmed'),
        ('Canceled', 'Canceled')
    )
    requester = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='delivery_requester',
                                  blank=True, null=True)
    provider = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='delivery_provider',
                                 blank=True, null=True)
    pickup_location = models.CharField(max_length=128)
    drop_off_location = models.CharField(max_length=128)
    deadline = models.DateField()
    status = models.CharField(choices=STATUS, max_length=64, default='Created, not accepted')
    title = models.CharField(max_length=128)
    text = models.TextField(max_length=512)
    image = models.ImageField(upload_to='deliveries', null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    is_checked = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.requester and self.requester.points < 20:
            if self.is_checked:
                super(Delivery, self).save(*args, **kwargs)
            return "Not enough points"
        else:
            super(Delivery, self).save(*args, **kwargs)


class RequestDelivery(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Canceled', 'Canceled'),
    )
    service = models.ForeignKey(Delivery, on_delete=models.CASCADE)
    requester = models.ForeignKey('users.User', on_delete=models.CASCADE, blank=True, null=True)
    status = models.CharField(choices=STATUS, max_length=64, default='Pending')
    accept = models.BooleanField(default=False)

    def __str__(self):
        return '%s' % self.service


@receiver(post_save, sender=Delivery)
def pull_delivery_points(sender, instance, created, **kwargs):
    if created and instance.requester:
        points = 20
        user = instance.requester
        user_points = user.points
        user_points -= points
        user.points = user_points
        user.save()


@receiver(post_save, sender=Delivery)
def pay_delivery_points(sender, instance, created, **kwargs):
    if instance.status == "Successfully done":
        points = 20
        user = instance.provider
        user_points = user.points
        user_points += points
        user.points = user_points
        user.save()


@receiver(post_save, sender=Delivery)
def delivery_cancel_notification(sender, instance, created, **kwargs):
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


class PickUp(models.Model):
    STATUS = (
        ('Created, not accepted', 'Created, not accepted'),
        ('Accepted/in process', 'Accepted/in process'),
        ('Successfully done', 'Successfully done'),
        ('Not confirmed', 'Not confirmed'),
        ('Canceled', 'Canceled')
    )
    requester = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='pickup_requester',
                                  null=True, blank=True)
    provider = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='pickup_provider',
                                 blank=True, null=True)
    pickup_location = models.CharField(max_length=128)
    drop_off_location = models.CharField(max_length=128)
    deadline = models.DateTimeField()
    status = models.CharField(choices=STATUS, max_length=64, default='Created, not accepted')
    title = models.CharField(max_length=128)
    text = models.TextField(max_length=512)
    image = models.ImageField(upload_to='pickups', null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    is_checked = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.requester.points < 20:
            if self.is_checked:
                super(PickUp, self).save(*args, **kwargs)
            return "Not enough points"
        else:
            super(PickUp, self).save(*args, **kwargs)


class RequestPickUp(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Canceled', 'Canceled'),
    )
    service = models.ForeignKey(PickUp, on_delete=models.CASCADE)
    requester = models.ForeignKey('users.User', on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS, max_length=64, default='Pending')
    accept = models.BooleanField(default=False)

    def __str__(self):
        return '%s' % self.service


@receiver(post_save, sender=PickUp)
def pull_pickup_points(sender, instance, created, **kwargs):
    if created:
        points = 20
        user = instance.requester
        user_points = user.points
        user_points -= points
        user.points = user_points
        user.save()


@receiver(post_save, sender=PickUp)
def pay_pickup_points(sender, instance, created, **kwargs):
    if instance.status == "Successfully done":
        points = 20
        user = instance.provider
        user_points = user.points
        user_points += points
        user.points = user_points
        user.save()


@receiver(post_save, sender=PickUp)
def pickup_cancel_notification(sender, instance, created, **kwargs):
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


class Hosting(models.Model):
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
    requester = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='hosting_requester',
                                  null=True, blank=True)
    provider = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='hosting_provider',
                                 blank=True, null=True)
    title = models.CharField(max_length=128)
    text = models.TextField(max_length=512)
    date = models.DateField()
    preferences = models.CharField(max_length=64, choices=PREFS)
    status = models.CharField(max_length=64, choices=STATUS, default='Created, not accepted')
    image = models.ImageField(upload_to='hostings', null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    is_checked = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.requester.points < 20:
            if self.is_checked:
                super(Hosting, self).save(*args, **kwargs)
            return "Not enough points"
        else:
            super(Hosting, self).save(*args, **kwargs)


class RequestHosting(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Canceled', 'Canceled'),
    )
    service = models.ForeignKey(Hosting, on_delete=models.CASCADE)
    requester = models.ForeignKey('users.User', on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS, max_length=64, default='Pending')
    accept = models.BooleanField(default=False)

    def __str__(self):
        return '%s' % self.service


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


@receiver(post_save, sender=Hosting)
def hosting_cancel_notification(sender, instance, created, **kwargs):
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


class Support(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField(unique=False)
    title = models.CharField(max_length=128)
    text = models.TextField(max_length=512)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return '%s %s' % (self.name, self.title)


class ProvideDelivery(models.Model):
    provider = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='delivery_prov',
                                 null=True, blank=True)
    requester = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='delivery_req',
                                  null=True, blank=True)
    departure_location = models.CharField(max_length=128)
    departure_date = models.DateField()
    arrival_location = models.CharField(max_length=128)
    arrival_date = models.DateField()
    title = models.CharField(max_length=64)
    text = models.TextField(max_length=640)
    created = models.DateField(auto_now_add=True)
    is_checked = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class ProvidePickUp(models.Model):
    provider = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='pickup_prov',
                                 null=True, blank=True)
    requester = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='pickup_req',
                                  null=True, blank=True)
    pickup_location = models.CharField(max_length=128)
    pickup_date = models.DateField()
    title = models.CharField(max_length=64)
    text = models.TextField(max_length=640)
    created = models.DateField(auto_now_add=True)
    is_checked = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class ProvideHosting(models.Model):
    HOSTING = (
        ('Private bedroom', 'Private bedroom'),
        ('Living room', 'Living room'),
        ('Common space', 'Common space'),
        ('Other', 'Other')
    )
    provider = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='hosting_prov',
                                 null=True, blank=True)
    requester = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='hosting_req',
                                  null=True, blank=True)
    location = models.CharField(max_length=128)
    hosting_date = models.DateField()
    title = models.CharField(max_length=64)
    hosting_type = models.CharField(max_length=64, choices=HOSTING)
    created = models.DateField(auto_now_add=True)
    is_checked = models.BooleanField(default=False)

    def __str__(self):
        return self.title
