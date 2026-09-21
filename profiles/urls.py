from django.urls import path
from .views import *

urlpatterns = [
    path('edit/my/', profiles_create, name='profiles_create'),
    path('<str:username>/', profiles_detail, name='profiles_detail'),
]