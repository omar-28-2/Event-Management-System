from django.db import models
from django.conf import settings  # Import settings to use AUTH_USER_MODEL

class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=200)
    vendor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='events')
    number_of_seats = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2 , default=0)

    def __str__(self):
        return self.name
