from django.urls import path
from .views import VideoListAPIView
# from .views import VideoViewSet
# from .views import get_video_list
# from .views import get_video
# from .views import index

urlpatterns = [
    path('all/', VideoListAPIView.as_view(), name='video-list'),
    # path('all/', get_video_list, name='video-list'),
    # path('all/', VideoViewSet.as_view({'get': 'list'}), name='video-list'),
    
]
