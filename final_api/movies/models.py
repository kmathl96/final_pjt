from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=30)

class Movie(models.Model):

    title = models.CharField(max_length = 50)
    original_title = models.CharField(max_length=150)
    release_date = models.DateField()
    popularity = models.FloatField(null=True, blank=True)
    vote_count = models.IntegerField()
    vote_average = models.FloatField(null=True, blank=True)
    adult = models.BooleanField()
    overview = models.TextField()
    original_language = models.CharField(max_length=80)
    poster_path = models.CharField(max_length=150)
    backdrop_path = models.CharField(max_length=150, null=True)
    genres = models.ManyToManyField(Genre, related_name = 'genre_name')
    liked_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')
    # rating_users = models.ManyToManyField(setting.AUTH_USER_MODEL, related_name='rating_movies')
    
class Rating(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rate = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    content = models.TextField()

# class GenreCount(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     Adventure = models.IntegerField(default=0)
#     Fantasy = models.IntegerField(default=0)
#     Animation = models.IntegerField(default=0)
#     Drama = models.IntegerField(default=0)
#     Horror = models.IntegerField(default=0)
#     Action = models.IntegerField(default=0)
#     Comedy = models.IntegerField(default=0)
#     History = models.IntegerField(default=0)
#     Western = models.IntegerField(default=0)
#     Triller = models.IntegerField(default=0)
#     Crime = models.IntegerField(default=0)
#     Documentary = models.IntegerField(default=0)
#     Science_fiction = models.IntegerField(default=0)
#     Mystery = models.IntegerField(default=0)
#     Music = models.IntegerField(default=0)
#     Romance = models.IntegerField(default=0)
#     Family = models.IntegerField(default=0)
#     War = models.IntegerField(default=0)
#     TV_movie = models.IntegerField(default=0)

# class GenreSum(models.Model):
#     # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     # genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
#     # sum_rate = models.IntegerField(default=0)
#     # count = models.IntegerField(default=0)
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     Adventure = models.IntegerField(default=0)
#     Fantasy = models.IntegerField(default=0)
#     Animation = models.IntegerField(default=0)
#     Drama = models.IntegerField(default=0)
#     Horror = models.IntegerField(default=0)
#     Action = models.IntegerField(default=0)
#     Comedy = models.IntegerField(default=0)
#     History = models.IntegerField(default=0)
#     Western = models.IntegerField(default=0)
#     Triller = models.IntegerField(default=0)
#     Crime = models.IntegerField(default=0)
#     Documentary = models.IntegerField(default=0)
#     Science_fiction = models.IntegerField(default=0)
#     Mystery = models.IntegerField(default=0)
#     Music = models.IntegerField(default=0)
#     Romance = models.IntegerField(default=0)
#     Family = models.IntegerField(default=0)
#     War = models.IntegerField(default=0)
#     TV_movie = models.IntegerField(default=0)
