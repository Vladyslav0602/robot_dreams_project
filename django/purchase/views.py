from .models import Purchase
from .serializers import PurchaseSerializer
from rest_framework import viewsets
from django_filters import rest_framework as filters


class PurchaseFilter(filters.FilterSet):
    user__username = filters.CharFilter(field_name='user__username', lookup_expr='icontains')
    book__title = filters.CharFilter(field_name='book__title', lookup_expr='icontains')
    purchase_date = filters.DateFilter()

    class Meta:
        model = Purchase
        fields = ['user__username', 'book__title', 'purchase_date']


class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    filterset_class = PurchaseFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        user__username = self.request.query_params.get('user__username')
        book__title = self.request.query_params.get('book__title')
        purchase_date = self.request.query_params.get('purchase_date')

        if user__username:
            queryset = queryset.filter(user__username__icontains=user__username)
        if book__title:
            queryset = queryset.filter(book__title__icontains=book__title)
        if purchase_date:
            queryset = queryset.filter(purchase_date=purchase_date)

        return queryset

# class PurchaseListView(ListView):
#     def get(self, request):
#         purchases = Purchase.objects.all()
#         return render(request, 'purchase/purchase_list.html', {'purchases': purchases})
#
#
# class PurchaseDetailView(DetailView):
#     def get(self, request, id):
#         purchase = get_object_or_404(Purchase, id=id)
#         return render(request, 'purchase/purchase_detail.html', {'purchase': purchase})
#
#
# class CreatePurchaseView(CreateView):
#     model = Purchase
#     template_name = 'purchase/create_purchase.html'
#     fields = ['user', 'book', 'purchase_date']
#
#     def get(self, request):
#         form = PurchaseForm()
#         return render(request, 'purchase/create_purchase.html', {'form': form})
#
#     def post(self, request):
#         form = PurchaseForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('purchase_list')
#         return render(request, 'purchase/create_purchase.html', {'form': form})


# class PurchaseView(generics.ListCreateAPIView):
#     queryset = Purchase.objects.all()
#     serializer_class = PurchaseSerializer
#
#
# class PurchaseDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Purchase.objects.all()
#     serializer_class = PurchaseSerializer


# def create_purchases(request):
#     # Отримуємо список користувачів та книжок, щоб створити зв'язані записи у таблиці "Purchase"
#     users = User.objects.all()
#     books = Book.objects.all()
#
#     # Створюємо список покупок для заповнення таблиці
#     purchases_to_create = [
#         Purchase(user=users[0], book=books[0], purchase_date=datetime.now()),
#         Purchase(user=users[1], book=books[1], purchase_date=datetime.now()),
#         Purchase(user=users[2], book=books[2], purchase_date=datetime.now()),
#         Purchase(user=users[3], book=books[3], purchase_date=datetime.now()),
#         Purchase(user=users[4], book=books[4], purchase_date=datetime.now()),
#     ]
#
#     # Зберігаємо об'єкти в базі даних
#     Purchase.objects.bulk_create(purchases_to_create)
#
#     return JsonResponse ("Дані про покупки були додані до бази даних.")
