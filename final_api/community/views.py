from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import Review, Comment
from .serializers import ReviewSerializer, ReviewListSerializer, CommentSerializer
# Create your views here.

@api_view(['GET'])
def index(request):
    reviews = Review.objects.all()
    serializer = ReviewListSerializer(reviews, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create(request):
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data)

@api_view(['GET'])
def detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    serializer = ReviewSerializer(review)
    return Response(serializer.data)

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if review.user == request.user:
        review.title = request.data.get('title', review.title)
        review.content = request.data.get('content', review.content)
        review.save()
        return Response('수정이 완료되었습니다.')

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def delete(request,review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if review.user == request.user:
        review.delete()
        return Response("성공하셨습니다.")

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_comment(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user, review=review)
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update_comment(request, review_pk, comment_pk):
    review = get_object_or_404(Review, pk=review_pk)
    comment = get_object_or_404(Comment, pk=comment_pk, review=review)
    if comment.user == request.user:
        comment.content = request.data.get('content', comment.content)
        comment.save()
        return Response('댓글 수정이 완료되었습니다.')

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def delete_comment(request, review_pk, comment_pk):
    review = get_object_or_404(Review, pk=review_pk)
    comment = get_object_or_404(Comment, pk=comment_pk, review=review)
    if comment.user == request.user:
        comment.delete()
        return Response("댓글 삭제를 완료하였습니다.")

@api_view(['GET'])
def comment_list(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    comments = Comment.objects.all().filter(review=review)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)