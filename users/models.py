# from django.contrib.auth.models import AbstractUser
# from django.db import models

# class User(AbstractUser):
#     name = models.CharField(null=False, blank=False, max_length=50)
#     email = models.EmailField(unique=True, null=False, blank=False)
#     password = models.CharField(max_length=50)
#     phone_number = models.CharField(max_length=17, null=True, blank=True)
#     Create_at = models.DateTimeField(auto_now_add=True)



from django.contrib.auth.models import AbstractUser, Group
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('librarian', 'Librarian'),
        ('member', 'Member'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='member')

    def __str__(self):
        return self.username





