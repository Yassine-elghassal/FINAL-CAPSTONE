from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from .models import Post
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Post.objects.filter(user=self.request.user)  # Only show posts of the logged-in user

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Follow

class FollowView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        following = request.data.get('following')
        follow = Follow(follower=request.user, following=following)
        follow.save()
        return Response({"message": "Followed successfully!"}, status=201)

    def delete(self, request):
        following = request.data.get('following')
        follow = Follow.objects.filter(follower=request.user, following=following)
        follow.delete()
        return Response({"message": "Unfollowed successfully!"}, status=204)

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post, Follow
from .serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated

class FeedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Get all followed users' posts
        followed_users = Follow.objects.filter(follower=request.user).values('following')
        posts = Post.objects.filter(user__in=followed_users).order_by('-timestamp')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
