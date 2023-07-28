from django.urls import path
from .views import users_view,  create_users

urlpatterns = [
    path('users/', users_view, name='users'),
    path('create_users/', create_users, name='create_users'),
]
