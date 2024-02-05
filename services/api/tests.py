from django.test import TestCase
from api.serializers import UserSerializer


class UserSerializerTest(TestCase):
    def test_valid_data(self):
        serializer = UserSerializer(data={"username": "abc887","email": "user123@example.com","password": "ddaasa","first_name": "John","last_name": "Doe","date_of_birth": "1990-01-01","phone_number": "1234567890"})
        self.assertTrue(serializer.is_valid())

    def test_invalid_data(self):
        serializer = UserSerializer(data={"password": "ddaasa","first_name": "John","last_name": "Doe","date_of_birth": "1990-01-01","phone_number": "1234567890"})
        self.assertFalse(serializer.is_valid())

