from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        # Додали унікальний індекс, який об'єднує поля "title" та "author"
        unique_together = ('title', 'author')

    def __str__(self):
        return f"{self.title} - {self.author}"

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'price': str(self.price),
        }
