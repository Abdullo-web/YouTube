from django.urls import path
from .views import *


urlpatterns = [
    path('profiles_create/',profiles_create, name='profiles_create'),
    path('profile/',profile, name='profile'),
]
