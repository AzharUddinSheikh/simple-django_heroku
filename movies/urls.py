from django.urls import path
from . import views

# so we dont need to name like movie_index django aware of this app_name use it in html by like this {% url "movie:index" %}
app_name = "movie"

urlpatterns = [
    path('home', views.home1, name="home1"),
    path('', views.index, name="index"),
    path('<int:movieid>', views.detail, name='detail')
]
