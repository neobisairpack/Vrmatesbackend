# Generated by Django 2.2 on 2020-09-14 05:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('services', '0002_auto_20200914_0458'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsersWorkInProvideService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_provider', models.BooleanField(default=False)),
                ('is_requester', models.BooleanField(default=False)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='provide_workers', to='services.ProvideService')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'service')},
            },
        ),
    ]
