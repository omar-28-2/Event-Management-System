from django.db import models

# Create your models here.

class ContactSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"Message from {self.name} ({self.email})"