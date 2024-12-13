from django.db import models

class CustomUser(models.Model):
    USER_TYPE_CHOICES = (
        ('vendor', 'Vendor'),
        ('user', 'User'),
    )

    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=15)
    password = models.CharField(max_length=100)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)

    def __str__(self):
        return self.username





