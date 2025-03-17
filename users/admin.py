from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import CustomUser

User = get_user_model() 

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'role')
    search_fields = ('username', 'email')
