from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    firstName = models.CharField(max_length=10, default="")
    lastName = models.CharField(max_length=10, default="")
    DOB = models.CharField(max_length=10, default="")
    mobile = models.CharField(max_length=10, default="")