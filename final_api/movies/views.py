from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import Movie, Genre,  Rating
from .serializers import MovieListSerializer, RatingSerializer, RatingListSerializer, GenreSerializer
# Create your views here.

@api_view(('GET',))
def index(request):
    movies = Movie.objects.all().order_by('-vote_count')
    serializer = MovieListSerializer(movies,many=True)
    return Response(serializer.data)
    
@api_view(('GET',))
def recommend_random(request):
    movies = Movie.objects.all().order_by('?')[:10]
    serializer = MovieListSerializer(movies,many=True)
    return Response(serializer.data)

@api_view(('GET',))
def genreinput(request):
    genres = Genre.objects.all()
    serializer = GenreSerializer(genres, many=True)
    return Response(serializer.data)

# @api_view(['POST'])
# def gcinput(request):
#     serializer = GenreCountSerializer(blank=True)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     return Response(serializer.errors)

# 평점
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def rating_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)

    serializer = RatingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user, movie=movie)
        # genre_count = GenreCount.objects.all().filter(user=request.user)
        
        # for genre in movie.genres.all():
        
        #     # genre_count = GenreCount.objects.all()
        #     # genre_count = get_object_or_404(GenreCount)
        #     print(genre_count)
        #     # genre_count.count += 1
        #     # genre_count.sum_rate += 1

        return Response(serializer.data)
    else:
        return Response(serializer.errors)

@api_view(['GET'])
def rating_list(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    ratings = Rating.objects.all().filter(movie=movie)
    serializer = RatingListSerializer(ratings, many=True)
    return Response(serializer.data)

    # movie = get_object_or_404(Movie, pk=movie_pk)
    # serializer = RatingSerializer()
    # genre_count = GenreCount.objects.all().filter(user=request.user)
    # if (Rating.objects.all().filter(movie=movie, user=request.user)).exists():
    #     return redirect('movies:detail', movie_pk)
    # else:
    #     for genre in genre_count:
    #         if genre in movie.genres.all():
    #             genre.count += 1
    #     genre_count.save()
    # return Response(serializer.data)

