import time
from celery import shared_task
from .models import CustomUser
from purchase.models import Purchase


@shared_task
def send_welcome_email():
    # Імітуємо відправку ласкаво просимо на сайт листа з привітанням.
    time.sleep(5)
    print("Welcome to Celery!")


@shared_task
def print_purchase_count(user_id):
    try:
        user = CustomUser.objects.get(pk=user_id)
        purchase_count = Purchase.objects.filter(user=user).count()
        print(f"User {user.username} has {purchase_count} purchases.")
    except CustomUser.DoesNotExist:
        print(f"User with ID {user_id} does not exist.")


@shared_task
def print_user_count():
    user_count = CustomUser.objects.count()
    print(f"Number of users in the database: {user_count}")
