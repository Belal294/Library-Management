from rest_framework.routers import SimpleRouter
from users.views import UserViewSet, LoginView, LogoutView, RegisterView
from books.views import BookViewSet, GenreViewSet, AuthorViewSet, BorrowViewSet, ReturnBookViewSet
from django.urls import path

router = SimpleRouter()

router.register('users', UserViewSet, basename='users')

router.register('books', BookViewSet, basename='books')
router.register('genres', GenreViewSet, basename='genres')
router.register('authors', AuthorViewSet, basename='authors')
router.register('borrow', BorrowViewSet, basename='borrow')
router.register('return', ReturnBookViewSet, basename='return')

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

urlpatterns += router.urls
