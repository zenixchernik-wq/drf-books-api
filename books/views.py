from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from .models import Book
from .serializers import BookSerializer


class BookViewSet(ModelViewSet):
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = Book.objects.all().order_by("id")

        big = self.request.query_params.get("big")
        category = self.request.query_params.get("category")

        if big == "true":
            queryset = queryset.filter(pages__gte=200)

        if category:
            queryset = queryset.filter(category_id=category)

        return queryset