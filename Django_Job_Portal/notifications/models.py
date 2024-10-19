from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User  # Assuming you're using Django's built-in User model

class Notification(models.Model):
    # Recipient of the notification
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')

    # Notification title and message
    title = models.CharField(max_length=255)
    message = models.TextField()

    # Optional link associated with the notification (e.g., link to the job or application)
    link = models.URLField(blank=True, null=True)

    # Notification Types (job-related, application-related, general, etc.)
    NOTIFICATION_TYPE_CHOICES = [
        ('Job', 'Job'),
        ('Application', 'Application'),
        ('General', 'General'),
        ('Reminder', 'Reminder'),
        ('Interview', 'Interview'),
    ]
    notification_type = models.CharField(max_length=50, choices=NOTIFICATION_TYPE_CHOICES)

    # Timestamp and read status
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification to {self.recipient.username}: {self.title}"

    # Method to mark notification as read
    def mark_as_read(self):
        self.is_read = True
        self.save()

