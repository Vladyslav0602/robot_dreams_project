from django.urls import path
from .views import purchases_view, create_purchases

urlpatterns = [
    path('purchases/', purchases_view, name='purchases'),
    path('create_purchases/', create_purchases, name='create_purchases'),
]
