from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from user_app.models import customUser
from rest_framework.authtoken.models import Token

class RegisterTestCase(APITestCase):
    def test_register(self):
        data = {
            'username': 'testcase',
            'first_name': 'test',
            'last_name': 'testing',
            'email': 'testcase@example.com',
            'password': 'Test_case1',
            'password2': 'Test_case1'
        }
        response = self.client.post(reverse('signup'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class LoginLogoutTestCase(APITestCase):

    def setUp(self):
        # Create a user with custom fields and ensure all necessary fields are filled in
        self.user = customUser.objects.create_user(
            username="example",
            password="example123",
            first_name="Test",
            last_name="User",
            email="example@example.com"
        )
        self.token = Token.objects.create(user=self.user)
        
        def test_login(self):
            data = {
                "username": "example",
                "password": "example123"
            }
            
            response = self.client.post(reverse('login'), data)
            print(response.data)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            
        def test_logout(self):
            self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
            response = self.client.post(reverse('logout'))
            print(response.data)
            self.assertEqual(response.status_code, status.HTTP_200_OK)