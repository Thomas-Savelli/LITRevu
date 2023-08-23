# Generated by Django 4.2.4 on 2023-08-23 07:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='follows',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='suit'),
        ),
    ]