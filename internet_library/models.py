from django.db import models
from django.utils import timezone

class Genre(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=60)
    date_of_birth = models.DateField()
    is_alive = models.BooleanField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Book(models.Model):
    title = models.CharField(max_length=255)
    date_of_creation = models.DateField()
    price = models.FloatField()
    pages_qty = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}, {self.author.first_name} {self.author.last_name}"
