from django.db import models
from accounts.models import Users
from django.contrib.postgres.fields import ArrayField


class CandidateProfile(models.Model):
    user = models.OneToOneField(Users, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    contact_number = models.CharField(max_length=15, blank=True, null=True)
    resume = models.FileField(upload_to='documents/resumes/', blank=True, null=True)
    profile_pic = models.ImageField(upload_to='documents/profile_pictures/', blank=True, null=True)

    bio = models.TextField(blank=True, null=True)
    education = models.CharField(max_length=255, blank=True, null=True)
    experience = models.TextField(blank=True, null=True)
    skills = ArrayField(models.CharField(max_length=50), blank=True, null=True)  # Skills as an array
    social_links = ArrayField(models.URLField(), blank=True, null=True)


# TODO: singles django