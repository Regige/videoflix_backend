from django.urls import path
from .views import VideoListAPIView


urlpatterns = [
    path('all/', VideoListAPIView.as_view(), name='video-list'),
]
