from django.db import models

# Create your models here.
class Movie(models.Model):
    resim = models.FileField(upload_to = 'movies', null=True, blank=True, verbose_name="Film resmi")
    title = models.CharField(max_length=200, verbose_name="Film adı")

    def __str__(self):
        return self.title