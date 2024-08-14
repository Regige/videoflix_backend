from django.shortcuts import render

from rest_framework import viewsets
from .models import Video
from .serializers import VideoSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.core.cache.backends.base import DEFAULT_TIMEOUT 
from django.views.decorators.cache import cache_page 
from django.conf import settings

from rest_framework.response import Response
from rest_framework import status

from rest_framework.decorators import api_view, permission_classes, authentication_classes


CACHETTL = getattr(settings, 'CACHETTL', DEFAULT_TIMEOUT)


@cache_page(CACHETTL)
class VideoViewSet(viewsets.ModelViewSet):
    
    authentication_classes = [JWTAuthentication] 
    permission_classes = [IsAuthenticated]
    
    serializer_class = VideoSerializer
    
    def get_queryset(self):
        return Video.objects.all()