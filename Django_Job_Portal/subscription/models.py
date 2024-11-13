from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()

class SubscriptionPlan(models.Model):
    PLAN_CHOICES = [
        ('free', 'Free'),
        ('basic', 'Basic'),
        ('professional', 'Professional'),
        ('premium', 'Premium'),
        ('enterprise', 'Enterprise')
    ]

    name = models.CharField(max_length=50, choices=PLAN_CHOICES, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    description = models.TextField(max_length=500)
    features = models.TextField(max_length=500)
    duration = models.DurationField(help_text="Duration of the plan as a timedelta object (e.g., 30 days).")
    max_job_applications_per_day = models.PositiveIntegerField(default=0)
    priority_support = models.BooleanField(default=False)
    career_coaching = models.BooleanField(default=False)
    create_at = models.DateTimeField(default=timezone.now)
    update_at = models.DateTimeField(auto_now=True)

    # todo: created_at and updated_at


class UserSubscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscriptions')
    plan = models.ForeignKey(SubscriptionPlan, on_delete=models.PROTECT)
    start_date = models.DateTimeField(default=timezone.now)
    auto_renew = models.BooleanField(default=True)
    has_expired = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    trial_start_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # todo: created_at and updated_at


    def save(self, *args, **kwargs):
        if self.plan and not self.trial_start_date:
            self.trial_start_date = self.start_date + self.plan.duration

        super(UserSubscription, self).save(*args, **kwargs)

