from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=20)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    readers = models.ManyToManyField(User, blank=True)

    class Meta:
        permissions = [
            ("can like book", "can_like_book"), 
            ("can unlike book", "can_unlike_book"),
        ]

    def __str__(self):
        return self.title