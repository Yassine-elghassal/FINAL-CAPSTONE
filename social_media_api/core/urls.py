from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, FollowView, FeedView

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/follow/', FollowView.as_view(), name='follow'),
    path('api/feed/', FeedView.as_view(), name='feed'),
]
