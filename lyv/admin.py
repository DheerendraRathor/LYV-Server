from django.contrib import admin
from .models import Book, Paragraph, Recording


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'language', 'filename']


@admin.register(Paragraph)
class ParagraphAdmin(admin.ModelAdmin):
    list_display = ['id', 'book', 'index', 'paragraph', 'recorded']


@admin.register(Recording)
class RecordingAdmin(admin.ModelAdmin):
    list_display = ['id', 'paragraph', 'filename']
