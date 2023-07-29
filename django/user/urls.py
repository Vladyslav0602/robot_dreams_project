from django.urls import path
from . import views
from .views import CustomUserDetailView, CustomUserView

urlpatterns = [
    # path('users/', CustomUserListView.as_view(), name='user_list'),
    # path('users/<int:pk>/', CustomUserDetailView.as_view(), name='user_detail'),
    # path('create_user/', CreateUserView.as_view(), name='create_user'),
    path('users/', CustomUserView.as_view(), name='user_list'),
    path('users/<int:pk>/', CustomUserDetailView.as_view(), name='user_detail'),
]

