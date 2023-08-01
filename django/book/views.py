from .serializers import BookSerializer
from rest_framework import viewsets
from .models import Book
from django_filters import rest_framework as filters


class BookFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')
    author = filters.CharFilter(lookup_expr='icontains')
    price = filters.NumberFilter()

    class Meta:
        model = Book
        fields = ['title', 'author', 'price']


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filterset_class = BookFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        title = self.request.query_params.get('title')
        author = self.request.query_params.get('author')
        price = self.request.query_params.get('price')

        if title:
            queryset = queryset.filter(title__icontains=title)
        if author:
            queryset = queryset.filter(author__icontains=author)
        if price:
            queryset = queryset.filter(price=price)

        return queryset

# class BookListView(ListView):
#     model = Book
#     template_name = 'book/book_list.html'
#     context_object_name = 'books'
#
#
# class BookDetailView(DetailView):
#     model = Book
#     template_name = 'book/book_detail.html'
#     context_object_name = 'book'
#
#
# class CreateBookView(CreateView):
#     model = Book
#     template_name = 'book/create_book.html'
#     fields = ['title', 'author', 'genre']
#
#     def get(self, request):
#         form = BookForm()
#         return render(request, 'book/create_book.html', {'form': form})
#
#     def post(self, request):
#         form = BookForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('book_list')
#         return render(request, 'book/create_book.html', {'form': form})


# class BookView(generics.ListCreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
#
# class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


# def create_books(request):
#     # Генеруємо рандомні ціни для кожної книги у діапазоні від 10 до 100
#     def generate_random_price():
#         return round(random.uniform(10, 100), 2)
#
#     # Створюємо список книжок для заповнення таблиці
#     books_to_create = [
#         Book(title='The Great Gatsby', author='F. Scott Fitzgerald', price=generate_random_price()),
#         Book(title='To Kill a Mockingbird', author='Harper Lee', price=generate_random_price()),
#         Book(title='1984', author='George Orwell', price=generate_random_price()),
#         Book(title='Pride and Prejudice', author='Jane Austen', price=generate_random_price()),
#         Book(title='Harry Potter and the Sorcerer\'s Stone', author='J.K. Rowling', price=generate_random_price()),
#     ]
#
#     # Зберігаємо об'єкти в базі даних
#     Book.objects.bulk_create(books_to_create)
#
#     return JsonResponse("Дані про книжки були додані до бази даних.")
