from django.db import models

class Category(models.Model):
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.category

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

  