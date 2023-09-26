from django.contrib import admin
from .models import UserMovieRating, UserMovieReview, Movie, Director, Cast, Genre
# Register your models here.

admin.site.register(UserMovieReview)
admin.site.register(UserMovieRating)
admin.site.register(Movie)
admin.site.register(Director)
admin.site.register(Cast)
admin.site.register(Genre)