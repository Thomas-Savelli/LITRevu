# Generated by Django 4.2.4 on 2023-09-14 18:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews_app', '0014_alter_critique_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='critique',
            name='note',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
