from rest_framework.test import APITestCase
from rest_framework import status
from rental.apps.users.models import User

class UserAuthentication(APITestCase):

    def test_create_super_user(self):
        user = User.objects.create_superuser(username='appadmin',
                                             password='appadminpassword',
                                             email='app@admin.com')
        self.assertEqual(user.is_staff, True)

    def test_register_user(self):
        data = {"user": {
                "username": "johndoe",
                "email": "johndoe@gmail.com",
                "password": "@IamTheOne!"}
                }
        response = self.client.post('/api/auth/register', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

   