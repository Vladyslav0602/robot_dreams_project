from django.http import JsonResponse
from user.models import User
from book.models import Book
from datetime import datetime
from .models import Purchase


def purchases_view(request):
    purchases = Purchase.objects.all()
    data = [{"user": purchase.user.name, "book": purchase.book.title, "purchase_date": purchase.purchase_date} for
            purchase in purchases]
    return JsonResponse(data, safe=False)


def create_purchases(request):
    # Отримуємо список користувачів та книжок, щоб створити зв'язані записи у таблиці "Purchase"
    users = User.objects.all()
    books = Book.objects.all()

    # Створюємо список покупок для заповнення таблиці
    purchases_to_create = [
        Purchase(user=users[0], book=books[0], purchase_date=datetime.now()),
        Purchase(user=users[1], book=books[1], purchase_date=datetime.now()),
        Purchase(user=users[2], book=books[2], purchase_date=datetime.now()),
        Purchase(user=users[3], book=books[3], purchase_date=datetime.now()),
        Purchase(user=users[4], book=books[4], purchase_date=datetime.now()),
    ]

    # Зберігаємо об'єкти в базі даних
    Purchase.objects.bulk_create(purchases_to_create)

    return JsonResponse ("Дані про покупки були додані до бази даних.")
