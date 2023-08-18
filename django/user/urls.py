from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet

router = DefaultRouter()
router.register(r'users', CustomUserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

# from django.urls import path
# from . import views
#
# urlpatterns = [
#     path('send_welcome_email/', views.send_welcome_email_view, name='send_welcome_email'),
#     path('print_purchase_count/<int:user_id>/', views.print_purchase_count_view, name='print_purchase_count'),
#     path('print_user_count/', views.print_user_count_view, name='print_user_count'),
#     path('task_result/<str:task_id>/', views.task_result_view, name='task_result'),
# ]


# from django.urls import path, include
# from .views import CustomUserViewSet
# from rest_framework.routers import DefaultRouter
#
#
# router = DefaultRouter()
# router.register(r'custom_users', CustomUserViewSet)
#
#
# urlpatterns = [
#     # path('users/', CustomUserListView.as_view(), name='user_list'),
#     # path('users/<int:pk>/', CustomUserDetailView.as_view(), name='user_detail'),
#     # path('create_user/', CreateUserView.as_view(), name='create_user'),
#     # path('users/', CustomUserView.as_view(), name='user_list'),
#     # path('users/<int:pk>/', CustomUserDetailView.as_view(), name='user_detail'),
#     path('', include(router.urls)),
#     path('filter_users/', CustomUserViewSet.as_view({'get': 'list'}), name='filter_user_list'),
# ]

