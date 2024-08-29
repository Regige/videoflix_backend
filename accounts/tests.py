from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()

class SignUpTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.sign_up_url = '/accounts/'  # Der URL-Pfad für den SignUp-Endpunkt

    def test_user_creation(self):
        """
        Testet, ob die SignUp-View einen Benutzer erfolgreich erstellt.
        """
        payload = {
            'username': 'test_user@example.com',
            'email': 'test_user@example.com',
            'password': 'test_password'
        }

        response = self.client.post(self.sign_up_url, payload, format='json')

        # Überprüfe, ob der Statuscode 201 Created zurückgegeben wird
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Überprüfe, ob der Benutzer in der Datenbank erstellt wurde
        user_exists = User.objects.filter(email='test_user@example.com').exists()
        self.assertTrue(user_exists)

        # Optional: Überprüfe, ob die Benutzerinformationen korrekt sind
        user = User.objects.get(email='test_user@example.com')
        self.assertEqual(user.username, 'test_user@example.com')