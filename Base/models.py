from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Director(models.Model):
    name = models.TextField()


class Cast(models.Model):
    name = models.TextField()


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.TextField()
    year_released = models.TextField(max_length=4)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    duration = models.IntegerField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    rating = models.IntegerField()
    cast = models.ManyToManyField(Cast)

    def __str__(self):
        return self.name


class UserMovieRating(models.Model):
    RATING_CHOICES = [
        (1, 'One Star'),
        (2, 'Two Stars'),
        (3, 'Three Stars'),
        (4, 'Four Stars'),
        (5, 'Five Stars'),
    ]

    rating = models.IntegerField(choices=RATING_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)


class UserMovieReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    review = models.TextField(null=False)
