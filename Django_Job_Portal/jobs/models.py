from django.db import models

from employers.models import EmployerProfile


class JobManager(models.Manager):

    def create_job(self, **extra_fields):
        job = self.model(**extra_fields)
        job.save()
        return job


class Job(models.Model):
    employer = models.ForeignKey(EmployerProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    TYPE_CHOICES = [
            ('Government', 'Government'),
        ('Private', 'Private'),
    ]
    job_type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    SUBTYPE_CHOICES = [
        ('Full-time', 'Full-time'),
        ('Part-time', 'Part-time'),
        ('Contract', 'Contract'),
        ('Internship', 'Internship'),
        ('Temporary', 'Temporary'),
        ('Freelance', 'Freelance'),
    ]
    job_subtype = models.CharField(max_length=50, choices=SUBTYPE_CHOICES)
    EXPERIENCE_LEVEL_CHOICES = [
        ('Entry', 'Entry Level'),
        ('Mid', 'Mid Level'),
        ('Senior', 'Senior Level'),
        ('Director', 'Director'),
        ('Executive', 'Executive'),
    ]
    experience_level = models.CharField(max_length=50, choices=EXPERIENCE_LEVEL_CHOICES)
    company_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255, blank=True, null=True)
    salary_range = models.CharField(max_length=50)
    posted_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True, null=True)
    application_link = models.URLField(blank=True, null=True)
    application_email = models.EmailField(blank=True, null=True)
    is_deleted = models.BooleanField(default=False)


    objects = JobManager()