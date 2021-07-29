from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    last_login = models.DateTimeField(default=timezone.now)
    last_request = models.DateTimeField(default=timezone.now)
