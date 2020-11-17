from django.db import models
from django.contrib.auth.models import AbstractUser
# from movies.models import GenreCount
# Create your models here.
class User(AbstractUser):
    # genrecount = models.OneToOneField(GenreCount, related_name = 'genre_count',on_delete=models.)
    # genrecount=models.oneto(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pass