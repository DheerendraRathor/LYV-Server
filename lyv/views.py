from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from core.pagination import DefaultCursorPagination

from .serializers import BookSerializer, ParagraphSerializer, RecordingSerializer
from .models import Book, Paragraph, Recording


class BookViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = DefaultCursorPagination


class ParagraphViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Paragraph.objects.all()
    serializer_class = ParagraphSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = DefaultCursorPagination


class RecordingViewSet(viewsets.ModelViewSet):
    queryset = Recording.objects.all()
    serializer_class = RecordingSerializer
    permission_classes = [IsAuthenticated]
