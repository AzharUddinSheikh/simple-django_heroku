from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="movie_index"),
    path('<int:movieid>', views.detail, name='movie_detail')
]
