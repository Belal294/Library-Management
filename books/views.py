from rest_framework import viewsets,status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, BasePermission
from .models import Book, Genre, Author,Borrow
from .serializers import BookSerializer, GenreSerializer, AuthorSerializer, BorrowSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone


class CustomPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['GET', 'POST', 'PUT', 'DELETE']:  
            return True
        

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [CustomPermission]
    


class BorrowViewSet(viewsets.ModelViewSet):
    queryset = Borrow.objects.all()
    serializer_class = BorrowSerializer
    

    def perform_create(self, serializer):
        book = serializer.validated_data['book']
        if not book.is_available():
            return Response({"error": "This book is not available for borrowing."}, status=status.HTTP_400_BAD_REQUEST)
        serializer.save(user=self.request.user)

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


