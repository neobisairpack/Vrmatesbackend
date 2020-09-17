from django.dispatch import receiver
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.db.models.signals import post_save

from services.models import *


@receiver(post_save, sender=RequestService)
def service_status(sender, instance, created, **kwargs):
    if instance.status == 'Accepted' or instance.accept:
        status = 'Accepted/in process'
        service = instance.service
        service.status = status
        service.provider = instance.requester
        service.save()


@receiver(post_save, sender=RequestService)
def user_request_service_create_role_check(sender, instance, created, **kwargs):
    if instance.status == 'Accepted':
        UsersWorkInService.objects.create(
            user=instance.requester, service=instance.service, is_provider=True, is_requester=False
        )


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
def user_service_requester_role_check(sender, instance, created, **kwargs):
    if created:
        UsersWorkInService.objects.create(
            user=instance.requester, service=instance, is_provider=False, is_requester=True
        )


@receiver(post_save, sender=Service)
def service_create_notification(sender, instance, created, **kwargs):
    if created:
        if instance.requester is not None:
            mail_subject = 'Post created| Vrmates team'
            message = render_to_string('services/service_created.html', {
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
            mail_subject = 'Post created | Vrmates team'
            message = render_to_string('services/service_created.html', {
                'user': instance.provider.first_name,
                'title': instance.title,
                'status': instance.status
            })
            to_email = instance.provider.email
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()


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


@receiver(post_save, sender=RequestProvideService)
def user_request_service_provide_role_check(sender, instance, created, **kwargs):
    if instance.status == 'Accepted':
        UsersWorkInProvideService.objects.create(
            user=instance.requester, service=instance.service, is_provider=False, is_requester=True
        )


@receiver(post_save, sender=RequestProvideService)
def provide_service_status(sender, instance, created, **kwargs):
    if instance.status == 'Accepted' or instance.accept:
        status = 'Accepted/in process'
        service = instance.service
        service.status = status
        service.requester = instance.requester
        service.save()


@receiver(post_save, sender=ProvideService)
def user_service_provide_requester_role_check(sender, instance, created, **kwargs):
    if created:
        UsersWorkInProvideService.objects.create(
            user=instance.provider, service=instance, is_provider=True, is_requester=False
        )


@receiver(post_save, sender=ProvideService)
def pull_service_provide_points(sender, instance, created, **kwargs):
    if instance.status == 'Accepted/in process' and instance.requester:
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
def provide_service_create_notification(sender, instance, created, **kwargs):
    if created:
        if instance.requester is not None:
            mail_subject = 'Post created| Vrmates team'
            message = render_to_string('services/service_created.html', {
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
            mail_subject = 'Post created | Vrmates team'
            message = render_to_string('services/service_created.html', {
                'user': instance.provider.first_name,
                'title': instance.title,
                'status': instance.status
            })
            to_email = instance.provider.email
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()


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
                'user': instance.provider.first_name,
                'title': instance.title,
                'status': instance.status
            })
            to_email = instance.provider.email
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
