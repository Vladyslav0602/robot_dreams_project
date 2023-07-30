from django.urls import path, include
from .views import CustomUserViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'custom_users', CustomUserViewSet)


urlpatterns = [
    # path('users/', CustomUserListView.as_view(), name='user_list'),
    # path('users/<int:pk>/', CustomUserDetailView.as_view(), name='user_detail'),
    # path('create_user/', CreateUserView.as_view(), name='create_user'),
    # path('users/', CustomUserView.as_view(), name='user_list'),
    # path('users/<int:pk>/', CustomUserDetailView.as_view(), name='user_detail'),
    path('', include(router.urls)),
    path('filter_users/', CustomUserViewSet.as_view({'get': 'list'}), name='filter_user_list'),
]