import json

from django.test import TestCase
from api.serializers import UserSerializer
from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model


class UserSerializerTest(TestCase):
    def test_valid_data(self):
        serializer = UserSerializer(data={"username": "abc887","email": "user123@example.com","password": "ddaasa","first_name": "John","last_name": "Doe","date_of_birth": "1990-01-01","phone_number": "1234567890"})
        self.assertTrue(serializer.is_valid())

    def test_invalid_data(self):
        serializer = UserSerializer(data={"password": "ddaasa","first_name": "John","last_name": "Doe","date_of_birth": "1990-01-01","phone_number": "1234567890"})
        self.assertFalse(serializer.is_valid())


class UserAPITest(APITestCase):
    def setUp(self):
        self.data = {"username": "testuser","email": "user123@example.com","password": "ddaasa","first_name": "John","last_name": "Doe"}
        self.user = get_user_model().objects.create_user(**self.data)
        # self.token = None

    def test_create_user(self):
        api_url = reverse("register")
        payload_data = {"username": "abc887","email": "user123@example.com","password": "ddaasa","first_name": "John","last_name": "Doe","date_of_birth": "1990-01-01","phone_number": "1234567890"}
        res = self.client.post(api_url, payload_data)
        self.assertEqual(res.status_code, 201)

    def test_get_token(self):
        token_url = reverse("token_obtain_pair")
        payload_data = {"username": self.data['username'], "password": self.data['password']}
        res = self.client.post(token_url, payload_data)
        json_res = json.loads(res.content.decode('utf-8'))
        self.assertEqual(res.status_code, 200)
        self.assertEqual(list(json_res.keys()), ['token'])
        print("json_res :: ", json_res)
        self.token = json_res['token']  # Corrected assignment line
        print("self.token :: ", self.token)

    def test_user_logout(self):
        self.test_get_token()
        logout_api = reverse('api-logout')
        headers = {'Authorization': f'Token {self.token}'}
        res = self.client.post(logout_api, headers=headers)
        self.assertEqual(res.status_code, 200)