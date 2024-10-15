from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

class Job(models.Model):
    # Job Information
    title = models.CharField(max_length=255)
    description = models.TextField()

    # Job Type (Government, Private, NGO, etc.)
    TYPE_CHOICES = [
        ('Government', 'Government'),
        ('Private', 'Private'),
        ('NGO', 'NGO'),
        ('Public', 'Public'),
        ('Nonprofit', 'Nonprofit'),
        ('Freelance', 'Freelance'),
    ]
    job_type = models.CharField(max_length=50, choices=TYPE_CHOICES)

    # Job Subtype (Full-time, Part-time, Contract, etc.)
    SUBTYPE_CHOICES = [
        ('Full-time', 'Full-time'),
        ('Part-time', 'Part-time'),
        ('Contract', 'Contract'),
        ('Internship', 'Internship'),
        ('Temporary', 'Temporary'),
        ('Freelance', 'Freelance'),
    ]
    job_subtype = models.CharField(max_length=50, choices=SUBTYPE_CHOICES)

    # Experience Level
    EXPERIENCE_LEVEL_CHOICES = [
        ('Entry', 'Entry Level'),
        ('Mid', 'Mid Level'),
        ('Senior', 'Senior Level'),
        ('Director', 'Director'),
        ('Executive', 'Executive'),
    ]
    experience_level = models.CharField(max_length=50, choices=EXPERIENCE_LEVEL_CHOICES)

    # Company and Location
    company_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255, blank=True, null=True)

    # Salary Information
    salary_min = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    salary_max = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    # Post and Deadline Information
    posted_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True, null=True)

    # Application Information
    application_link = models.URLField(blank=True, null=True)
    application_email = models.EmailField(blank=True, null=True)

    # Applicant Limits
    applicant_limit = models.PositiveIntegerField(blank=True, null=True)

