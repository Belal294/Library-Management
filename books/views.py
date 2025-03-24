from rest_framework import viewsets,status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, BasePermission
from .models import Book, Genre, Author,Borrow, Review, BooksImage
from .serializers import BookSerializer, GenreSerializer, AuthorSerializer, BorrowSerializer, SimpleUserSerializer, ReviewSerializer, BooksImageSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from rest_framework.permissions import IsAdminUser, AllowAny
from api.permissions import IsAdminOrReadOnly
from rest_framework.permissions import DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly
from rest_framework.viewsets import ModelViewSet
from books.permissions import IsReviewAuthorOrReadonly
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema


# class CustomPermission(BasePermission):
#     def has_permission(self, request, view):
#         if request.method in ['GET', 'POST', 'PUT', 'DELETE']:  
#             return True
        

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [DjangoModelPermissions]

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    # permission_classes = [IsAdminOrReadOnly]
    permission_classes = [DjangoModelPermissions]


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminOrReadOnly]
    
    # def get_permissions(self):
    #     if self.request.method=='GET':
    #         return [AllowAny()]
    #     return [IsAdminUser()]

    @swagger_auto_schema(
            operation_summary= 'Retrive A list of Books'
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    

    @swagger_auto_schema(
            oparation_summary = "Create a product by admin"
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    

class BorrowViewSet(viewsets.ModelViewSet):
    queryset = Borrow.objects.all()
    serializer_class = BorrowSerializer
    permission_classes = [DjangoModelPermissions]
    

    def perform_create(self, serializer):
        book = serializer.validated_data['book']
        if not book.is_available():
            return Response({"error": "This book is not available for borrowing."}, status=status.HTTP_400_BAD_REQUEST)
        serializer.save(user=self.request.user)


class BooksImageViewSet(ModelViewSet):
    serializer_class = BooksImageSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        return BooksImage.objects.filter(books_id=self.kwargs.get('book_pk'))

    def perform_create(self, serializer):
        book = get_object_or_404(Book, id=self.kwargs.get('book_pk')) 
        serializer.save(books=book)


class ReturnBookViewSet(viewsets.ViewSet):

    def update(self, request, pk=None):
        try:
            borrow_instance = Borrow.objects.get(pk=pk, user=request.user, is_returned=False)
        except Borrow.DoesNotExist:
            return Response({"error": "Borrow record not found."}, status=status.HTTP_404_NOT_FOUND)

        borrow_instance.return_date = timezone.now().date()
        borrow_instance.is_returned = True
        borrow_instance.fine_amount = borrow_instance.calculate_fine()
        borrow_instance.book.available_copies += 1  
        borrow_instance.book.save()
        borrow_instance.save()

        return Response({"message": "Book returned successfully!", "fine": borrow_instance.fine_amount}, status=status.HTTP_200_OK)





class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [IsReviewAuthorOrReadonly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        books_pk = self.kwargs.get('books_pk')
        if books_pk:
            return Review.objects.filter(books_id=books_pk)
        else:
            return Review.objects.all() 

    def get_serializer_context(self):
        books_pk = self.kwargs.get('books_pk')
        return {'books_id': books_pk}
    


