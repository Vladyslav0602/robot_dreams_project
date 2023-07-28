from django.db import models
from user.models import User
from book.models import Book


class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField()

    class Meta:
        # Змінили порядок сортування на спадання за датою
        ordering = ['-purchase_date']

    def __str__(self):
        return f"{self.user.name} - {self.book.title} - {self.purchase_date}"

    def serialize(self):
        return {
            'user': self.user.name,
            'book': self.book.title,
            'purchase_date': self.purchase_date.strftime('%Y-%m-%d %H:%M:%S'),
        }
