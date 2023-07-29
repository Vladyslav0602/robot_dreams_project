from django.urls import path
from .views import BookDetailView, BookView

urlpatterns = [
    # path('books/', BookListView.as_view(), name='book_list'),
    # path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    # path('create_book/', CreateBookView.as_view(), name='create_book'),
    path('books/', BookView.as_view(), name='book_list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
]
