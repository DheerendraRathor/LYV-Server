from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    name = models.CharField(max_length=128)
    language = models.CharField(max_length=64)
    #filename = filefield

    def __str__(self):
        return self.name


class Paragraph(models.Model):
    book = models.ManyToManyField(Book, related_name='paragraphs')
    index = models.IntegerField(unique=True)
    recording = models.OneToOneField(Recording, related_name='recorded')


class Recording(models.Model):
    paragraph = models.ManyToManyField(Paragraph, related_name='recordings')
    #filename = filefield

