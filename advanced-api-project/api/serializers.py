# api/serializers.py

from rest_framework import serializers
from .models import Author, Book
from datetime import date

class BookSerializer(serializers.ModelSerializer):
    """
    A serializer for the Book model that handles validation for publication year.
    """
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year']

    def validate_publication_year(self, value):
        """
        Custom validation to ensure the publication year is not in the future.
        """
        if value > date.today().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    """
    A serializer for the Author model that includes a nested serializer for related books.
    This demonstrates handling a one-to-many relationship in the API response.
    """
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']