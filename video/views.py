from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from .models import Video
from .serializers import VideoSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.core.cache.backends.base import DEFAULT_TIMEOUT 
from django.views.decorators.cache import cache_page 
from django.utils.decorators import method_decorator
from django.conf import settings
from django.core.cache import cache

from rest_framework.response import Response
from rest_framework import status

from rest_framework.decorators import api_view, permission_classes, authentication_classes


CACHETTL = getattr(settings, 'CACHETTL', DEFAULT_TIMEOUT)



# # @vary_on_cookie
# @authentication_classes([JWTAuthentication])
# @permission_classes([IsAuthenticated])
# # @cache_page(CACHETTL)
# @cache_page(60 * 15)
# @api_view(["GET"])
# def get_video_list(request):
#     queryset = Video.objects.all()
#     serializer = VideoSerializer(queryset, many=True)
#     return Response(serializer.data)



class VideoListAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    # @method_decorator(cache_page(CACHETTL))
    def get(self, request, *args, **kwargs):
        queryset = Video.objects.all()
        serializer = VideoSerializer(queryset, many=True)
        return Response(serializer.data)
    
   
    

# class VideoListAPIView(APIView):
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsAuthenticated]

#     # @method_decorator(cache_page(CACHETTL))
#     def get(self, request, *args, **kwargs):
#         cache_key = 'videos_all'
#         cached_videos = cache.get(cache_key)

#         if cached_videos is None:
#             queryset = Video.objects.all()
#             serializer = VideoSerializer(queryset, many=True)
#             cache.set(cache_key, serializer.data, timeout=CACHETTL)
#         else:
#             serializer_data = cached_videos
#         return Response(serializer.data)




# @cache_page(CACHETTL)
# class VideoViewSet(viewsets.ReadOnlyModelViewSet):
    
#     authentication_classes = [JWTAuthentication] 
#     permission_classes = [IsAuthenticated]
    
#     serializer_class = VideoSerializer
    
#     def get_queryset(self):
#         return Video.objects.all()