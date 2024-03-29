from django.db import models
from user.models import CustomUser
from book.models import Book


class Purchase(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField()

    class Meta:
        # Змінили порядок сортування на спадання за датою
        ordering = ['-purchase_date']

    def __str__(self):
        return f"{self.user.username} - {self.book.title} - {self.purchase_date}"

    def serialize(self):
        return {
            'user': self.user.username,
            'book': self.book.title,
            'purchase_date': self.purchase_date.strftime('%Y-%m-%d %H:%M:%S'),
        }