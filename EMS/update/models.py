from django.db import models
from django.conf import settings  # To use the custom user model

class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,  # This will point to the custom user model or the default User model
        on_delete=models.CASCADE
    )
    phone_number = models.CharField(max_length=11, blank=True, null=True)  # Example field
    address = models.TextField(blank=True, null=True)  # Another example field

    def __str__(self):
        return self.user.username

