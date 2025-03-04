from django.db import models
from django.db.models import CharField


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    author = models.CharField(max_length=255)

    def __str__(self):
        return self.title
