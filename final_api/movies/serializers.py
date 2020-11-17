from rest_framework import serializers
from accounts.serializers import UserSerializer
from .models import Movie, Rating, Genre

class MovieListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = '__all__'

class RatingSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)


    class Meta:
        model = Rating
        fields = ['user','movie' ,'rate', 'content']
        read_only_fields = ('id','movie')

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

# class GenreCountSerializer(serializers.ModelSerializer):
#     user = UserSerializer()

#     class Meta:
#         model = GenreCount
#         fields = '__all__'

class RatingListSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Rating
        fields = '__all__'