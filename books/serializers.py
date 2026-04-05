from rest_framework import serializers
from .models import Book, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class BookSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source="category",
        write_only=True
    )
    is_big = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ["id", "title", "author", "pages", "category", "category_id", "is_big"]

    def get_is_big(self, obj):
        return obj.pages >= 200