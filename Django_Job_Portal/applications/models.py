from django.db import models

from accounts.models import Users
from jobs.models import Job
from candidates.models import CandidateProfile

class JobApplication(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    candidate = models.ForeignKey(CandidateProfile, on_delete=models.CASCADE, related_name='applications')
    application_date = models.DateTimeField(auto_now_add=True)

    # JobApplication.objects.filter(candidate__user__id=request.user.id)

    STATUS_CHOICES = [
        ('applied', 'Applied'),
        ('selected', 'Selected'),
        ('interviewed', 'Interviewed'),
        ('offered', 'Offered'),
        ('rejected', 'Rejected'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='applied')
    cover_letter = models.TextField(blank=True, null=True)
    resume = models.FileField(upload_to='documents/job_applications/', blank=True, null=True)

# TODO: STATUS UPDATE API NEED BASED ON CANDIDATE APPLIED