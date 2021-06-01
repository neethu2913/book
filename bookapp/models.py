from django.db import models

# Create your models here.
class Book(models.Model):
    book_name=models.CharField(max_length=120)
    author=models.CharField(max_length=120)
    price=models.CharField(max_length=120)
    pages=models.CharField(max_length=120)
    def __str__(self):
        return self.price