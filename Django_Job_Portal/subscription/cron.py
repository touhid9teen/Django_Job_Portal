from django.utils import timezone
from django_cron import CronJobBase, Schedule
from .models import UserSubscription


class SubscriptionCronJob(CronJobBase):

    schedule = Schedule(run_every_mins=10)
    code = 'cron.subscriptionCronJob'

    def do(self):
        subscription = UserSubscription.objects.filter(is_active=True)

        for subscription in subscription:
            if subscription.trial_start_date >= timezone.now():
                if subscription.auto_renew is True:
                    subscription.start_date = timezone.now()
                    subscription.trial_start_date = timezone.now() + subscription.plan.duration
                    subscription.save()
                elif subscription.auto_renew is False:
                    subscription.has_expired = True
                    subscription.is_active = False
                    subscription.save()


