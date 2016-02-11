from rest_framework import serializers
from .models import Book, Paragraph, Recording


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book


class ParagraphSerializer(serializers.ModelSerializer):

    class Meta:
        model = Paragraph


class RecordingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recording
