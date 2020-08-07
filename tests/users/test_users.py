from rest_framework.test import APITestCase
from rest_framework import status
from rental.apps.users.models import User


class Users(APITestCase):

    def test_create_super_user(self):
        user = User.objects.create_superuser(username='theadmin',
                                             password='theadminpa55word.',
                                             email='theadmin@admin.com')
        self.assertEqual(user.is_staff, True)

    def test_return_str__method(self):
        self.user = User.objects.create_user(
            username="test", email="test@gmail.com", password='t35t123')
        self.assertEqual(self.user.__str__(), 'test@gmail.com')

    def test_return_short_name__method(self):
        self.user = User.objects.create_user(
            username="test", email="test@gmail.com", password='t35t123')
        self.assertEqual('test', self.user.get_short_name())

    def test_return_full_name__method(self):
        self.user = User.objects.create_user(
            username="test", email="test@gmail.com", password='t35t123')
        self.assertEqual('test', self.user.get_full_name())
