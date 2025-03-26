from rest_framework import serializers
from .models import Book, Genre, Author,Borrow, Review, BooksImage
from django.contrib.auth import get_user_model

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
    


class BooksImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()
    class Meta:
        model = BooksImage
        fields = ['id','image']


class BookSerializer(serializers.ModelSerializer):
    images = BooksImageSerializer(many= True, read_only =True)
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'genre', 'available_copies', 'images']




class SimpleUserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(
        method_name='get_current_user_name')

    class Meta:
        model = get_user_model()
        fields = ['id', 'name']

    def get_current_user_name(self, obj):
        return obj.get_full_name()



class ReviewSerializer(serializers.ModelSerializer):
    # user = SimpleUserSerializer()
    user = serializers.SerializerMethodField(method_name='get_user')

    class Meta:
        model = Review
        fields = ['id', 'user', 'books', 'ratings', 'comment']
        read_only_fields = ['user', 'books']

    def get_user(self, obj):
        return SimpleUserSerializer(obj.user).data

    def create(self, validated_data):
        books_id = self.context['books_id']
        return Review.objects.create(books_id=books_id, **validated_data)
    



