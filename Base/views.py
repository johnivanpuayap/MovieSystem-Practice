from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie, Genre


# Create your views here.

def home_page(request):
    movies = Movie.objects.all()
    genres = Genre.objects.all()

    context = {
        'movies': movies,
        'genres': genres,
    }

    return render(request, 'home.html', context)
