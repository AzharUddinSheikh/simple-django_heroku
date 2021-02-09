from django.db import models
from django.utils import timezone

# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=50)
    year = models.IntegerField()
    rating = models.FloatField()
    stock_available = models.IntegerField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    date_created = models.DateField(default=timezone.now)
