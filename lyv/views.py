from django.shortcuts import get_object_or_404
from requests import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from core.pagination import DefaultCursorPagination
from rest_framework.decorators import detail_route
from core.mixins import SerializerClassRequestContextMixin

from .serializers import BookSerializer, ParagraphSerializer, RecordingSerializer
from .models import Book, Paragraph, Recording


class BookViewSet(SerializerClassRequestContextMixin, viewsets.ReadOnlyModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = DefaultCursorPagination

    @detail_route(permission_classes=[IsAuthenticated], pagination_class=DefaultCursorPagination)
    def get_paragraphs(self, request, pk):
        """
        Get paginated paragraphs of a book id
        ---
        response_serializer: ParagraphSerializer
        """
        book = get_object_or_404(Book, pk=pk)
        paragraphs = Paragraph.objects.filter(book=book).all()
        paragraphs = self.paginate_queryset(paragraphs)
        paragraphs = self.get_context_serializer_class(ParagraphSerializer, paragraphs, many=True)
        return self.get_paginated_response(paragraphs.data)


class ParagraphViewSet(SerializerClassRequestContextMixin, viewsets.ReadOnlyModelViewSet):
    queryset = Paragraph.objects.all()
    serializer_class = ParagraphSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = DefaultCursorPagination

    @detail_route(permission_classes=[], pagination_class=DefaultCursorPagination)
    def get_recordings(self, request, pk):
        """
        Get paginated recordings of a paragraph id
        ---
        response_serializer: ParagraphSerializer
        """
        paragraph = get_object_or_404(Paragraph, pk=pk)
        recordings = Recording.objects.filter(paragraph=paragraph).all()
        recordings = self.paginate_queryset(recordings)
        recordings = self.get_context_serializer_class(RecordingSerializer, recordings, many=True)
        return self.get_paginated_response(recordings.data)


class RecordingViewSet(viewsets.ModelViewSet):
    queryset = Recording.objects.all()
    serializer_class = RecordingSerializer
    permission_classes = [IsAuthenticated]
