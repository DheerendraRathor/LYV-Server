from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class LanguageChoices(object):
    English = 'English'
    Hindi = 'Hindi'
    Marathi = 'Marathi'
    Punjabi = 'Punjabi'
    Bengali = 'Bengali'
    Telugu = 'Telugu'
    Tamil = 'Tamil'
    Kannada = 'Kannada'

    @classmethod
    def to_dict(cls):
        return {
            cls.English: 'English',
            cls.Hindi: 'Hindi',
            cls.Marathi: 'Marathi',
            cls.Punjabi: 'Punjabi',
            cls.Bengali: 'Bengali',
            cls.Telugu: 'Telugu',
            cls.Tamil: 'Tamil',
            cls.Kannada: 'Kannada',
        }

    @classmethod
    def choices(cls):
        return [(v, v) for k, v in cls.to_dict().items()]



class Book(models.Model):
    name = models.CharField(max_length=128)
    language = models.CharField(max_length=64, choices=LanguageChoices.choices())
    filename = models.FileField(upload_to='books')

    def __str__(self):
        return self.name


class Paragraph(models.Model):
    book = models.ForeignKey(Book, related_name='paragraphs')
    index = models.IntegerField()
    paragraph = models.TextField()
    recorded = models.BooleanField(default=False)

    class Meta:
        unique_together = ('book', 'index')


class Recording(models.Model):
    paragraph = models.ForeignKey(Paragraph, related_name='recordings')
    filename = models.FileField(upload_to='recordings')
    user = models.ForeignKey(User, related_name='user_recording')


def get_paragraph_splits(file):
    file.open('rb')
    MIN_PARAGRAPH_LENGTH = 50
    lines = file.read().decode('utf-8').splitlines()
    actual_paragraphs = []

    current_line = ''
    for line in lines:
        line = ' '.join(line.split())
        current_line = line if current_line == '' else '\n'.join([current_line, line])
        if len(current_line.split()) > MIN_PARAGRAPH_LENGTH:
            actual_paragraphs.append(current_line)
            current_line = ''

    if current_line != '':
        actual_paragraphs.append(current_line)

    return actual_paragraphs


@receiver(post_save, sender=Book)
def book_file_handler(sender, instance: Book, **kwargs):
    paragraphs = get_paragraph_splits(instance.filename)
    index = 1
    for paragraph in paragraphs:
        paragraph_item = Paragraph(book=instance, paragraph=paragraph, recorded=False, index=index)
        paragraph_item.save()
        index += 1
