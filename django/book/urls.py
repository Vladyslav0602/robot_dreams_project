from django.urls import path
from .views import books_view, create_books

urlpatterns = [
    path('books/', books_view, name='books'),
    path('create_books/', create_books, name='create_books'),
]
