from django.urls import path
from .views import *


urlpatterns = [
    path('register/',register_usero, name='register'),
    path('login/',login_usero, name='login'),
    path('logaut/',logaut_user, name='logaut'),
]
