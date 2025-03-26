from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import timedelta
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator, FileExtensionValidator
from books.validators import validate_file_size
from cloudinary.models import CloudinaryField

User = get_user_model()

class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

def get_default_genre():
    genre, created = Genre.objects.get_or_create(name="Unknown")
    return genre.id

class Book(models.Model):
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('borrowed', 'Borrowed'),
        ('reserved', 'Reserved'),
    ]

    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, default=get_default_genre)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='available')
    available_copies = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.title

    def is_available(self):
        return self.available_copies > 0  


def get_due_date():
    return timezone.now() + timedelta(days=14)


class BooksImage(models.Model):
    books = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='images')
    # image = models.ImageField(upload_to="books/images/", validators=[validate_file_size])
    image = CloudinaryField('image')


class Borrow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateField(auto_now_add=True)
    due_date = models.DateField(default=get_due_date)
    return_date = models.DateField(null=True, blank=True)
    is_returned = models.BooleanField(default=False)
    fine_amount = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.user.username} borrowed {self.book.title}"

    def save(self, *args, **kwargs):
        if not self.is_returned and self.book.is_available():
            self.book.available_copies -= 1
            self.book.save()
        super().save(*args, **kwargs)

    def calculate_fine(self):
        if not self.is_returned and timezone.now().date() > self.due_date:
            overdue_days = (timezone.now().date() - self.due_date).days
            return overdue_days * 5
        return 0


class Review(models.Model):
    books = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ratings = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=5)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return f"Review By {self.user.first_name} on {self.books.title}"