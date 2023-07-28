from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'price')
    search_fields = ('title', 'author')


admin.site.register(Book, BookAdmin)
