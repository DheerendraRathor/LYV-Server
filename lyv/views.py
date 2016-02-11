from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination, CursorPagination
from rest_framework.permissions import IsAuthenticated

from .serializers import BookSerializer, ParagraphSerializer, RecordingSerializer
from .models import Book, Paragraph, Recording


class BookViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = CursorPagination


class ParagraphViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Paragraph.objects.all()
    serializer_class = ParagraphSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = LimitOffsetPagination


class RecordingViewSet(viewsets.ModelViewSet):
    queryset = Recording.objects.all()
    serializer_class = RecordingSerializer
    permission_classes = [IsAuthenticated]
