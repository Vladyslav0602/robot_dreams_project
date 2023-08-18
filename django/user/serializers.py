from rest_framework.pagination import PageNumberPagination
from rest_framework import serializers
from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}


class CustomUserPagination(PageNumberPagination):
    page_size = 10
