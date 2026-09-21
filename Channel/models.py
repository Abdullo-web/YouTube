from django.db import models
from accounts.models import Users

class Channels(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    avatar = models.ImageField(upload_to='avatar_channel')
    owner = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='channels')

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    video_file = models.FileField(upload_to='video_user')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    channel = models.ForeignKey(Channels, on_delete=models.CASCADE, related_name='videos')
    cr_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Like(models.Model):
    like_users = models.ForeignKey(Users, on_delete=models.CASCADE)
    like_video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='likes')

    class Meta:
        unique_together = ('like_users', 'like_video')


class Comment(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    cr_at = models.DateTimeField(auto_now_add=True)
    comment_id = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')

    def __str__(self):
        return f'{self.user.username} {self.text}'


class Follow(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    channel = models.ForeignKey(Channels, on_delete=models.CASCADE, related_name='channel_follow')

    class Meta:
        unique_together = ('user', 'channel')