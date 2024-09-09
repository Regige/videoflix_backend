from django.shortcuts import render

from rest_framework.generics import ListAPIView, GenericAPIView
from rest_framework import response,status
from rest_framework.response import Response
from . import serializers, models
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
import jwt
from .utils import Util

from django.conf import settings
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from django.shortcuts import redirect
from django.template.loader import render_to_string


class SignUp(GenericAPIView):

    serializer_class = serializers.SignUpSerializer

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        newUser = serializer.save()
        user = serializer.data
        
        # Setze das Passwort sicher
        newUser.set_password(request.data['password'])
        newUser.save()

        # getting tokens
        user_email = models.CustomUser.objects.get(email=user['email'])
        tokens = RefreshToken.for_user(user_email).access_token
        # send email for user verification
        current_site = get_current_site(request).domain
        relative_link = reverse('email-verify')
        absurl = 'http://'+current_site+relative_link+"?token="+str(tokens)
        email_body = render_to_string('verify_email.html', {
            'username': user['username'],
            'verification_link': absurl,
        })

        data = {'email_body': email_body, 'to_email': user['email'],
                'email_subject': 'Verify your email'}

        Util.send_email(data=data)

        return response.Response({'user_data': user, 'access_token' : str(tokens)}, status=status.HTTP_201_CREATED)


class VerifyEmail(GenericAPIView ):
    serializer_class = serializers.EmailVerificationSerializer

    token_param_config = openapi.Parameter(
        'token', in_=openapi.IN_QUERY, description='Description', type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[token_param_config])
    def get(self, request):
        token = request.GET.get('token')
        try:
            payload = jwt.decode(token, options={"verify_signature": False})
            print(payload)
            user = models.CustomUser.objects.get(id=payload['user_id'])
            if not user.is_verified:
                user.is_verified = True
                user.save()

            return redirect('https://videoflix.regina-gering.com/main-page')
        except jwt.ExpiredSignatureError as identifier:
            return redirect('https://videoflix.regina-gering.com/error?message=Activation Expired')
        except jwt.exceptions.DecodeError as identifier:
            return redirect('https://videoflix.regina-gering.com/error?message=Invalid Token')

