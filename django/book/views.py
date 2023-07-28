from django.http import JsonResponse
from .models import Book
import random


def books_view(request):
    books = Book.objects.all()
    data = [{"title": book.title, "author": book.author} for book in books]
    return JsonResponse(data, safe=False)


def create_books(request):
    # Генеруємо рандомні ціни для кожної книги у діапазоні від 10 до 100
    def generate_random_price():
        return round(random.uniform(10, 100), 2)

    # Створюємо список книжок для заповнення таблиці
    books_to_create = [
        Book(title='The Great Gatsby', author='F. Scott Fitzgerald', price=generate_random_price()),
        Book(title='To Kill a Mockingbird', author='Harper Lee', price=generate_random_price()),
        Book(title='1984', author='George Orwell', price=generate_random_price()),
        Book(title='Pride and Prejudice', author='Jane Austen', price=generate_random_price()),
        Book(title='Harry Potter and the Sorcerer\'s Stone', author='J.K. Rowling', price=generate_random_price()),
    ]

    # Зберігаємо об'єкти в базі даних
    Book.objects.bulk_create(books_to_create)

    return JsonResponse ("Дані про книжки були додані до бази даних.")
