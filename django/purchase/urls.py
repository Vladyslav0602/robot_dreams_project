from django.urls import path
from .views import PurchaseDetailView, PurchaseView

urlpatterns = [
    # path('purchases/', PurchaseListView.as_view(), name='purchase_list'),
    # path('purchases/<int:id>/', PurchaseDetailView.as_view(), name='purchase_detail'),
    # path('create_purchase/', CreatePurchaseView.as_view(), name='create_purchase'),
    path('purchases/', PurchaseView.as_view(), name='purchase_list'),
    path('purchases/<int:pk>/', PurchaseDetailView.as_view(), name='purchase_detail'),
]
