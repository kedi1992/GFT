# users/serializers.py

from rest_framework import serializers
from django.contrib.auth import get_user_model

from api.models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name', 'DOB', 'mobile')
        extra_kwargs = {'password': {'write_only': True}}

    # create user object
    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        return user

    # validate username
    def validate_username(self, value):
        if CustomUser.objects.filter(username=value).exists():
            raise serializers.ValidationError('Username must be unique.')
        return value

    # validate password
    def validate_password(self, value):
        if not value:
            raise serializers.ValidationError('Password should not blank')
        return value