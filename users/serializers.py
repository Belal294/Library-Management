# from rest_framework import serializers
# from django.contrib.auth import authenticate
# from .models import CustomUser
# from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer, UserSerializer as BaseUserSerializer


# # class RegisterSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = CustomUser
# #         fields = ['id', 'username', 'email', 'password', 'role']
# #         extra_kwargs = {'password': {'write_only': True}}

# #     def create(self, validated_data):
# #         user = CustomUser.objects.create_user(**validated_data)
# #         return user

# # class LoginSerializer(serializers.Serializer):
# #     username = serializers.CharField()
# #     password = serializers.CharField(write_only=True)

# #     def validate(self, data):
# #         user = authenticate(username=data['username'], password=data['password'])
# #         if not user:
# #             raise serializers.ValidationError("Invalid credentials")
# #         return user

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         ref_name = 'CustomUser'
#         model = CustomUser
#         fields = ['id', 'username', 'email', 'role']



# class UserCreateSerializer (BaseUserCreateSerializer):
#     class Meta(BaseUserCreateSerializer.Meta):
        
#         fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name']

# class UserSerializer(BaseUserCreateSerializer):
#     class Meta(BaseUserCreateSerializer.Meta):
#         ref_name = 'CustomUser'
#         fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name']




from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import CustomUser
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer, UserSerializer as BaseUserSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        ref_name = 'CustomUser'
        model = CustomUser
        fields = ['id', 'username', 'email', 'role']  

class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        model = CustomUser  
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name', 'role']  
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        if not user:
            raise serializers.ValidationError("Invalid credentials")
        return user

class CustomUserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        ref_name = 'CustomUser' 
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name', 'role']
