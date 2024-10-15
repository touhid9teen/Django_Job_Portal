from django.db import models
from accounts.models import Users  # Import the User model


class EmployerProfile(models.Model):
    user = models.OneToOneField(Users, on_delete=models.CASCADE)  # Link to User model
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.TextField()
    website = models.URLField(blank=True)
    company_name = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)  # Field for profile picture
