# Generated by Django 4.2.4 on 2023-08-22 08:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews_app', '0006_alter_critique_ticket'),
    ]

    operations = [
        migrations.RenameField(
            model_name='critique',
            old_name='headline',
            new_name='commentaire',
        ),
        migrations.RenameField(
            model_name='critique',
            old_name='rating',
            new_name='note',
        ),
    ]