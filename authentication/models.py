from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):

    profile_photo = models.ImageField(verbose_name='Photo de profil')
    follows = models.ManyToManyField(
        'self',
        symmetrical=False,
        verbose_name='suit',
        related_name='followed_by'
    )

    def __str__(self):
        return f'{self.username}'
