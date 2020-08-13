# Generated by Django 3.0.7 on 2020-08-13 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0006_auto_20200813_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='pickup_location',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='deliveryimage',
            name='image',
            field=models.FileField(upload_to='deliveries'),
        ),
    ]
