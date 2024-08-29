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
from django.views.decorators.vary import vary_on_cookie, vary_on_headers


CACHETTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


class VideoListAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @method_decorator(cache_page(CACHETTL))
    @method_decorator(vary_on_headers("Authorization"))
    def get(self, request, *args, **kwargs):
        queryset = Video.objects.all()
        serializer = VideoSerializer(queryset, many=True)
        return Response(serializer.data)
    
