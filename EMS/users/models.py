from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    user_type = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.username
