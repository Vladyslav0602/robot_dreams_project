from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import CustomUser

CustomUser = get_user_model()


class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Створення тестового користувача для всього класу тестів
        cls.test_user = CustomUser.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpassword'
        )

    def test_user_creation(self):
        # Перевірка чи об'єкт CustomUser був створений
        self.assertTrue(isinstance(self.test_user, CustomUser))
