from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie

# Create your views here.


def index(request):
    movies = Movie.objects.all()
    return render(request, 'movies/index.html', {'movies': movies})


def detail(request, movieid):
    details = Movie.objects.get(pk=movieid)
    return render(request, "movies/detail.html", {"details": details})
