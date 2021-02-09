from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Movie

# Create your views here.


def index(request):
    movies = Movie.objects.all()
    return render(request, 'movies/index.html', {'movies': movies})


def detail(request, movieid):

    details = get_object_or_404(Movie, pk=movieid)
    return render(request, "movies/detail.html", {"details": details})
