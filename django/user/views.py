from django.http import JsonResponse
from .models import User


# def users_view(request):
#     return HttpResponse("Hello, users!")


def users_view(request):
    users = User.objects.all()
    data = [{"name": user.name, "email": user.email} for user in users]
    return JsonResponse(data, safe=False)


def create_users(request):
    # Створюємо список користувачів для заповнення таблиці
    users_to_create = [
        User(name='John', email='john@example.com'),
        User(name='Alice', email='alice@example.com'),
        User(name='Bob', email='bob@example.com'),
        User(name='Mary', email='mary@example.com'),
        User(name='Michael', email='michael@example.com'),
        User(name='Emma', email='emma@example.com'),
        User(name='David', email='david@example.com'),
        User(name='Olivia', email='olivia@example.com'),
        User(name='William', email='william@example.com'),
        User(name='Sophia', email='sophia@example.com'),
    ]

    # Зберігаємо об'єкти в базі даних
    User.objects.bulk_create(users_to_create)

    return JsonResponse("Дані про користувачів були додані до бази даних.")
