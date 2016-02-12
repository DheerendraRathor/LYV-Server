from rest_framework import serializers
from .models import Book, Paragraph, Recording


class BookSerializer(serializers.ModelSerializer):
    recorded_paragraphs = serializers.SerializerMethodField()
    recorded_count = serializers.IntegerField(source='recorded_paragraphs')
    paragraph_count = serializers.IntegerField(source='recorded_count')
    
    def get_recorded_paragraphs(self, book: Book):
        return book.paragraphs.all().filter(recorded=True).count()

    class Meta:
        model = Book
        fields = ['id', 'name', 'language', 'filename', 'recorded_count', 'paragraph_count']



class ParagraphSerializer(serializers.ModelSerializer):

    class Meta:
        model = Paragraph


class RecordingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recording


class NewRecordingSerializer(serializers.Serializer):
    paragraph = serializers.PrimaryKeyRelatedField(queryset=Paragraph.objects.all())
    filename = serializers.FileField()
