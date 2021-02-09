from django.db import models
from tastypie.resources import ModelResource
from movies.models import Movie

# Create your models here.
# this class represt the concept of a movie in restapi


class MovieResource(ModelResource):
    class Meta:
        # queryset is not returing data from data base its simply return query & it ll execute near in the future that what we call lazy loading
        # so this object is lazy object which tastypie look for it inside meta class only
        queryset = Movie.objects.all()
        # how our endpoint loook like
        resource_name = "movies"
