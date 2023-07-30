from django.urls import path, include
from .views import PurchaseViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'purchases', PurchaseViewSet)


urlpatterns = [
    # path('purchases/', PurchaseListView.as_view(), name='purchase_list'),
    # path('purchases/<int:id>/', PurchaseDetailView.as_view(), name='purchase_detail'),
    # path('create_purchase/', CreatePurchaseView.as_view(), name='create_purchase'),
    # path('purchases/', PurchaseView.as_view(), name='purchase_list'),
    # path('purchases/<int:pk>/', PurchaseDetailView.as_view(), name='purchase_detail'),
    path('', include(router.urls)),
    path('filter_purchases/', PurchaseViewSet.as_view({'get': 'list'}), name='filter_purchase_list'),
]