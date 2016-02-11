from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    name = models.CharField(max_length=128)
    language = models.CharField(max_length=64)
    filename = models.FileField(upload_to='books')

    def __str__(self):
        return self.name


class Paragraph(models.Model):
    book = models.ForeignKey(Book, related_name='paragraphs')
    index = models.IntegerField(unique=True)


class Recording(models.Model):
    paragraph = models.ForeignKey(Paragraph, related_name='recordings')
    #filename = filefield

