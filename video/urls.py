from django.urls import path
from .views import VideoListAPIView
# from .views import get_video_list

urlpatterns = [
    path('all/', VideoListAPIView.as_view(), name='video-list'),
    # path('all/', get_video_list, name='video-list'),
]
