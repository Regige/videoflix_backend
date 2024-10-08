from django.urls import path, include
from . import views

from rest_framework.authtoken.views import obtain_auth_token

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', views.SignUp.as_view() , name='signup' ),
    path('email-verify/', views.VerifyEmail.as_view(), name="email-verify"),  
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
]
