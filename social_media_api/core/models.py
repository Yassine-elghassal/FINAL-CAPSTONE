from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class UserProfile(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)

from django.db import models
from django.contrib.auth import get_user_model

class Post(models.Model):
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='posts')
    media = models.URLField(blank=True, null=True)  # For media URLs

    def __str__(self):
        return f"Post by {self.user.username} at {self.timestamp}"

class Follow(models.Model):
    follower = models.ForeignKey(get_user_model(), related_name='following', on_delete=models.CASCADE)
    following = models.ForeignKey(get_user_model(), related_name='followers', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('follower', 'following')

    def __str__(self):
        return f"{self.follower.username} follows {self.following.username}"
