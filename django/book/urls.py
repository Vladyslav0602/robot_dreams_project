from django.urls import path
from .views import BookListView, BookDetailView, CreateBookView

urlpatterns = [
    path('books/', BookListView.as_view(), name='book_list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('create_book/', CreateBookView.as_view(), name='create_book'),
]
