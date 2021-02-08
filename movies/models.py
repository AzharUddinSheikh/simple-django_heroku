from django.db import models

# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=20)


class Movie(models.Model):
    title = models.CharField(max_length=50)
    year = models.IntegerField()
    rating = models.FloatField()
    stock_available = models.IntegerField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
