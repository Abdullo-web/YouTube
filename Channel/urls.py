from django.urls import path
from .views import *

urlpatterns = [
    path('', video_list, name='video_list'),
    path('video/<int:id>/', video_detail, name='video_detail'),
    path('video/<int:id>/like/', like_video, name='like_video'),
    path('video/<int:id>/comment/', comment_create, name='comment_create'),
    path('channel/create/', create_channel, name='create_channel'),
    path('channel/<int:id>/', channel_detail, name='channel_detail'),
    path('channel/<int:id>/follow/', follow_channel, name='follow_channel'),
    path('channel/<int:id>/add_video/', video_create, name='video_create'),
]