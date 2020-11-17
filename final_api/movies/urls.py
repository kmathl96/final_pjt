from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.index, name="index"),
    path('recommend_random/', views.recommend_random, name="recommend_random"),
    # path('genreinput/', views.genreinput, name="genreinput"),
    # path('gcinput/', views.gcinput, name="gcinput"),
    path('<int:movie_pk>/rate/', views.rating_create, name="rating_create"),
    path('<int:movie_pk>/rating_list/', views.rating_list, name="rating_list"),
]