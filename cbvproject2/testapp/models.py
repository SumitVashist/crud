from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=256)
    author=models.CharField(max_length=64)
    pages=models.PositiveIntegerField()
    price=models.FloatField()
