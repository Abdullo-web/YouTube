from django.urls import path
from .views import *


urlpatterns = [
    path('create_channel/',create_channel, name='create_channel'),

]
