from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    USERNAME_FIELD = 'email'
    email = models.EmailField(unique=True)
    REQUIRED_FIELDS = ['username']

    avatar = models.ImageField(upload_to='avatar', height_field=None, width_field=None, max_length=None, blank=True, null=True)