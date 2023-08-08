import time
from celery import shared_task
from .models import CustomUser
from purchase.models import Purchase


@shared_task
def send_welcome_email():
    # Імітуємо відправку ласкаво просимо на сайт листа з привітанням.
    # time.sleep(5)
    result = "Welcome email sent!"
    print(result)
    return result


@shared_task
def print_purchase_count(user_id):
    try:
        user = CustomUser.objects.get(pk=user_id)
        purchase_count = Purchase.objects.filter(user__id=user_id).count()
        result = f"User {user.username} has {purchase_count} purchases."
        print(result)
        return result
    except CustomUser.DoesNotExist:
        result = f"User with ID {user_id} does not exist."
        print(result)
        return result


@shared_task
def print_user_count():
    user_count = CustomUser.objects.count()
    result = f"Number of users in the database: {user_count}"
    print(result)
    return result
