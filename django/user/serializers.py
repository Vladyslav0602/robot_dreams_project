from rest_framework import serializers
from .models import CustomUser
from rest_framework.pagination import PageNumberPagination


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


class CustomUserPagination(PageNumberPagination):
    page_size = 10