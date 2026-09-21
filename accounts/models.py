from django.db import models
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):
    is_verified = models.BooleanField(default=False)
    code = models.CharField(max_length=50,null=True)
    bio = models.TextField()
    avatar = models.ImageField(upload_to='user_avatar')
    
    
    def __str__(self):
        return self.username
    
