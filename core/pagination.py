from rest_framework.pagination import CursorPagination


class DefaultCursorPagination(CursorPagination):
    page_size = 25
    ordering = 'id'

class RecordingCursorPagination(CursorPagination):
    page_size = 100
    ordering = 'id'
