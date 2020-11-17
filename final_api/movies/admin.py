from django.contrib import admin
from .models import Movie, Genre, Rating

class GenreAdmin(admin.ModelAdmin):
    list_display=['name']
admin.site.register(Genre, GenreAdmin)

class MovieAdmin(admin.ModelAdmin):
    list_display=['title', 'release_date']
admin.site.register(Movie, MovieAdmin)
# admin.site.register(GenreCount)
admin.site.register(Rating)
