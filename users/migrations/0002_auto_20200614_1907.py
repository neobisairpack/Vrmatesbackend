# Generated by Django 3.0.7 on 2020-06-14 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='rate',
            field=models.FloatField(null=True),
        ),
    ]
