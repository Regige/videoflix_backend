from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class VideoListAPIViewTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='test_user', password='test_password')
        self.token = self.get_jwt_token(self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

    def get_jwt_token(self, user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)

    def test_get_videos(self):
        """
        Testet, ob die VideoListAPIView einen Statuscode 200 zurückgibt, wenn sie aufgerufen wird.
        """
        response = self.client.get('/videos/all/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)