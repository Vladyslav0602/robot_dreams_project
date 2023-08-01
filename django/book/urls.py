from django.urls import path, include
from .views import BookViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'books', BookViewSet)


urlpatterns = [
    # path('books/', BookListView.as_view(), name='book_list'),
    # path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    # path('create_book/', CreateBookView.as_view(), name='create_book'),
    # path('books/', BookView.as_view(), name='book_list'),
    # path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('', include(router.urls)),
    path('filter_books/', BookViewSet.as_view({'get': 'list'}), name='filter_book_list'),
]