# Generated by Django 3.0.7 on 2020-08-13 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0005_auto_20200813_0609'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='delivery',
            name='provider',
        ),
        migrations.RemoveField(
            model_name='hosting',
            name='provider',
        ),
        migrations.RemoveField(
            model_name='pickup',
            name='provider',
        ),
        migrations.RemoveField(
            model_name='providedelivery',
            name='requester',
        ),
        migrations.RemoveField(
            model_name='providehosting',
            name='requester',
        ),
        migrations.RemoveField(
            model_name='providepickup',
            name='requester',
        ),
    ]
