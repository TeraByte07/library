from rest_framework import serializers
from catalogue_app.models import Author, Book, Borrowed_books
class authorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"

class BookSerializer(serializers.ModelSerializer):
    author = authorSerializer()
    class Meta:
        model = Book
        fields = "__all__"

    def create(self, validated_data):
        author_data = validated_data.pop('author')
        author, created = Author.objects.get_or_create(**author_data)
        book = Book.objects.create(author=author, **validated_data)
        return book

class BorrowedBooksSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)
    class Meta:
        model = Borrowed_books
        fields = ['book', 'user', 'borrowed_date', 'return_date']
