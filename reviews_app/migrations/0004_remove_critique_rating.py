# Generated by Django 4.2.4 on 2023-08-17 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews_app', '0003_rename_headline_critique_title_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='critique',
            name='rating',
        ),
    ]
