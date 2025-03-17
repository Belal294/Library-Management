from rest_framework import serializers
from .models import Book, Genre, Author,Borrow

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'  

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    genre = GenreSerializer()
    author = AuthorSerializer()

    class Meta:
        model = Book
        fields = '__all__'

class BorrowSerializer(serializers.ModelSerializer):
    fine_amount = serializers.SerializerMethodField()

    class Meta:
        model = Borrow
        fields = ['id', 'user', 'book', 'borrow_date', 'due_date', 'return_date', 'is_returned', 'fine_amount']

    def get_fine_amount(self, obj):
        return obj.calculate_fine()

    def validate(self, data):
        if not data['book'].is_available():
            raise serializers.ValidationError("This book is not available for borrowing.")
        return data

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'genre', 'available_copies']
