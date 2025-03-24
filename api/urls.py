from django.urls import path, include
from rest_framework.routers import SimpleRouter, DefaultRouter
from rest_framework_nested.routers import NestedSimpleRouter, NestedDefaultRouter

from rest_framework.response import Response
from rest_framework.decorators import api_view

from users.views import UserViewSet, LogoutView
from books.views import (
    BookViewSet, GenreViewSet, AuthorViewSet, BorrowViewSet,
    ReturnBookViewSet, ReviewViewSet, BooksImageViewSet
)


router = DefaultRouter()
router.register('users', UserViewSet, basename='users')
router.register('books', BookViewSet, basename='books')
router.register('genres', GenreViewSet, basename='genres')
router.register('authors', AuthorViewSet, basename='authors')
router.register('borrow', BorrowViewSet, basename='borrow')
router.register('return-book', ReturnBookViewSet, basename='return-book')
router.register('reviews', ReviewViewSet, basename='reviews')

books_router = NestedDefaultRouter(router, 'books', lookup='book')
books_router.register('images', BooksImageViewSet, basename='book-images')

@api_view(['GET'])
def api_info(request):
    return Response({
        'message': 'Welcome to the Library Management API!',
        'status': 'Running',
    })


urlpatterns = [
    path('logout/', LogoutView.as_view(), name='logout'),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),

    path('info/',api_info, name='api-info'),
    path('', include(router.urls)),
    path('', include(books_router.urls)),
]


