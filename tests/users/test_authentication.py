from rest_framework.test import APITestCase
from rest_framework import status
from rental.apps.users.models import User

class Authentication(APITestCase):
    def test_registration(self):
        """
        Test creation of a new user account
        """
        data = {
                "user": {
                    "username": "lydia",
                    "email": "lydia@gmail.com",
                    "password": "1yd1an5anyu"}
                }
        response = self.client.post('/api/auth/register', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_login(self):
        """
        Test logging into a user account
        """
        registration_data = {
                "user": {
                    "username": "lydia",
                    "email": "lydia@gmail.com",
                    "password": "1yd1an5anyu"}
                }
        self.client.post('/api/auth/register', registration_data, format='json')
        login_data = {
                "user": {
                    "email": "lydia@gmail.com",
                    "password": "1yd1an5anyu"}
                }
        login_response = self.client.post('/api/auth/login', login_data, format='json')
        self.assertEqual(login_response.status_code, status.HTTP_200_OK)