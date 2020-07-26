# Generated by Django 3.0.7 on 2020-07-21 12:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('services', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='provider',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_provider', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='service',
            name='requester',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_requester', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='hosting',
            name='provider',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hosting_provider', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='hosting',
            name='requester',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hosting_requester', to=settings.AUTH_USER_MODEL),
        ),
    ]
