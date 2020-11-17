from rest_framework import serializers
from accounts.serializers import UserSerializer
from .models import Review,Comment

class ReviewListSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Review
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at')

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)

    class Meta:
        model = Comment
        fields = ['id','user', 'review', 'content']
        read_only_fields = ('id', 'review')
        # read_only_fields = ('id','review', 'created_at', 'updated_at')