from django.db import models
from accounts.models import Users

class Channel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    avatar = models.ImageField(upload_to='avatar_channel')
    owner = models.ForeignKey(Users, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
