from django.urls import path
from .views import PurchaseListView, PurchaseDetailView, CreatePurchaseView


urlpatterns = [
    path('purchases/', PurchaseListView.as_view(), name='purchase_list'),
    path('purchases/<int:id>/', PurchaseDetailView.as_view(), name='purchase_detail'),
    path('create_purchase/', CreatePurchaseView.as_view(), name='create_purchase'),
]
