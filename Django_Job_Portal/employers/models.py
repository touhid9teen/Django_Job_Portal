from django.db import models
from accounts.models import Users  # Import the User model


class EmployerProfile(models.Model):
    user = models.OneToOneField(Users, on_delete=models.CASCADE, related_name='employer')
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    company_name = models.CharField(max_length=100, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)