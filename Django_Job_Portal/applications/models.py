from django.db import models
from django.utils import timezone

class Application(models.Model):
    # Foreign key to the Job model (Assumes you have a Job model)
    job = models.ForeignKey('Job', on_delete=models.CASCADE, related_name='applications')

    # Applicant Information
    applicant_name = models.CharField(max_length=255)
    applicant_email = models.EmailField()
    cover_letter = models.TextField(blank=True, null=True)

    # Resume and Attachments
    resume = models.FileField(upload_to='resumes/')
    portfolio_link = models.URLField(blank=True, null=True)

    # Status of Application
    APPLICATION_STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Reviewed', 'Reviewed'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
    ]
    status = models.CharField(max_length=50, choices=APPLICATION_STATUS_CHOICES, default='Pending')

    # Date of Application
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.applicant_name} - {self.job.title}"

    # Method to check if the application is still active (you can define what "active" means in your case)
    def is_active(self):
        return self.status == 'Pending'

