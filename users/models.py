import jwt
import datetime

from datetime import datetime, timedelta
from django.db import models
from django.conf import settings
from django.core.mail import EmailMessage
from django.core.paginator import Paginator
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.dispatch import receiver
from django.template.loader import render_to_string

from services import models as service_models


class MyUserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise TypeError("Please, enter your email.")

        user = self.model(
            username=username,
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(
            username=username,
            email=email,
            password=password,
        )
        user.is_active = True
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    USER_GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others')
    )
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    username = models.CharField(max_length=64, unique=True, null=True, blank=True)
    email = models.EmailField(unique=True)
    birthday = models.DateField(null=True)
    gender = models.CharField(max_length=16, choices=USER_GENDER)
    phone = models.CharField(max_length=64, unique=True)
    country = models.CharField(max_length=128, null=True, blank=True)
    zip_code = models.CharField(max_length=32, null=True, blank=True)
    state = models.CharField(max_length=128, null=True, blank=True)
    city = models.CharField(max_length=128, null=True, blank=True)
    address = models.CharField(max_length=128, null=True, blank=True)
    about_me = models.TextField(max_length=512, null=True, blank=True)
    image = models.ImageField(upload_to='users', null=True, blank=True)
    points = models.PositiveIntegerField(default=20)
    is_banned = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ]

    objects = MyUserManager()

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    @property
    def token(self):
        return self._generate_jwt_token()

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    def _generate_jwt_token(self):
        dt = datetime.now() + timedelta(days=60)
        token = jwt.encode({
            'id': self.pk,
            'exp': dt.utcfromtimestamp(dt.timestamp())
        }, settings.SECRET_KEY, algorithm='HS256')
        return token.decode('utf-8')

    def rating_count(self):
        ratings = Rating.objects.filter(provider=self)
        return len(ratings)

    def avg_rating(self):
        summary = 0
        ratings = Rating.objects.filter(provider=self)

        for rating in ratings:
            summary += rating.rating

        if len(ratings) > 0:
            return summary / len(ratings)
        else:
            return 0

    def avg_rating_last_ten(self):
        ratings = Rating.objects.filter(provider=self).order_by('-id')

        try:
            paginator = Paginator(ratings, 10)
            last_ten_ratings = paginator.page(1).object_list

            return sum(rating.rating for rating in last_ten_ratings) / len(last_ten_ratings)

        except ZeroDivisionError:
            return 0

    def canceled_posts_count(self):
        delivery = service_models.Delivery.objects.filter(requester=self, status='Canceled').count()
        pickup = service_models.PickUp.objects.filter(requester=self, status='Canceled').count()
        hosting = service_models.Hosting.objects.filter(requester=self, status='Canceled').count()
        return delivery + pickup + hosting

    avg_rating.short_description = 'Average rating'
    rating_count.short_description = 'Rating count'
    avg_rating_last_ten.short_description = 'Last ten'
    canceled_posts_count.short_description = 'Canceled posts'


@receiver(post_save, sender=User)
def banned_notifications(sender, instance, created, **kwargs):
    if instance.is_banned:
        instance.is_active = False
        mail_subject = 'Your account has been banned | Vrmates team'
        message = render_to_string('users/account_ban.html', {
            'user': instance.first_name
        })
        to_email = instance.email
        email = EmailMessage(
            mail_subject, message, to=[to_email]
        )
        email.send()


class Rating(models.Model):
    requester = models.ForeignKey('users.User', verbose_name='rater', on_delete=models.CASCADE, related_name='give_rate')
    provider = models.ForeignKey('users.User', verbose_name='receiver', on_delete=models.CASCADE, related_name='receive_rate')
    rating = models.FloatField(validators=(MinValueValidator(1.0), MaxValueValidator(5.0)))
    text = models.TextField(max_length=512)
    image = models.ImageField(upload_to='ratings')
    date = models.DateField(auto_now_add=True)
