from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'date_joined')
    search_fields = ('username', 'email')


admin.site.register(CustomUser, CustomUserAdmin)
