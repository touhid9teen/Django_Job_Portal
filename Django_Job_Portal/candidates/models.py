from django.db import models
from accounts.models import Users
from django.contrib.postgres.fields import ArrayField


class CandidateProfile(models.Model):
    user = models.OneToOneField(Users, on_delete=models.CASCADE, related_name='candidate')
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    address = models.TextField(max_length=100, blank=True, null=True)
    profile_pic = models.ImageField(upload_to='documents/profile_pictures/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    social_links = ArrayField(models.URLField(), blank=True, null=True)
    gender = models.CharField(max_length=100, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)



class CandidateSkills(models.Model):
    candidate = models.OneToOneField(CandidateProfile, on_delete=models.CASCADE, related_name='skills')
    resume = models.FileField(upload_to='documents/resumes/', blank=True, null=True)
    education = ArrayField(models.CharField(max_length=500), blank=True, null=True)
    experience = ArrayField(models.CharField(max_length=500), blank=True, null=True)
    skills = ArrayField(models.CharField(max_length=500), blank=True, null=True)
    languages = ArrayField(models.CharField(max_length=100), blank=True, null=True)
    projects = ArrayField(models.CharField(max_length=500), blank=True, null=True)
    certificate = ArrayField(models.CharField(max_length=500), blank=True, null=True)
    awards = ArrayField(models.CharField(max_length=500), blank=True, null=True)
    club_and_committee = ArrayField(models.CharField(max_length=500), blank=True, null=True)
    Competitive_exams = ArrayField(models.CharField(max_length=500), blank=True, null=True)