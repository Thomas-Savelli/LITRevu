from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

from PIL import Image

# Create your models here.


class Ticket(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=2048, blank=True)
    uploader = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
    has_critique = models.BooleanField(default=False)

    IMAGE_MAX_SIZE = (800, 800)

    def resize_image(self):
        if self.image:
            image = Image.open(self.image)
            image.thumbnail(self.IMAGE_MAX_SIZE)
            # Sauvegarde de l 'image redimensionnée dans le systeme de fichier
            # Ceci n'est pas la méthode save() du modele ...
            image.save(self.image.path)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.resize_image()

    def __str__(self):
        return f'{self.title}'


class Critique(models.Model):
    ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE, null=True, related_name="critiques")
    note = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    commentaire = models.CharField(max_length=128)
    body = models.TextField(max_length=8192, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
    contributors = models.ManyToManyField(
        settings.AUTH_USER_MODEL, through='CritiqueContributor', related_name='contributions')

    def __str__(self):
        return f'{self.ticket}'


class CritiqueContributor(models.Model):
    contributor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    critique = models.ForeignKey(Critique, on_delete=models.CASCADE)
    contribution = models.CharField(max_length=255, blank=True)

    class meta:
        # Garanti l'unicité de CritiqueContributor pour chaque contributor - critique
        unique_together = ('contributor', 'critique')
