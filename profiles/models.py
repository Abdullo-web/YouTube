from django.db import models
from accounts.models import Users
class Profiles(models.Model):
    owner_profile = models.OneToOneField(Users, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatar_profile')
    bio = models.TextField()
    
    def __str__(self):
        return self.owner_profile.username
    