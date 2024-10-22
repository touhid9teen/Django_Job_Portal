from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Users
from candidates.models import CandidateProfile
from employers.models import EmployerProfile

# todo: otp verified then signals apply

@receiver(post_save, sender=Users)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == 'candidate':
            CandidateProfile.objects.create(user=instance)
        elif instance.user_type == 'employer':
            EmployerProfile.objects.create(user=instance)


@receiver(post_save, sender=Users)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type == 'candidate':
        instance.candidateprofile.save()
    elif instance.user_type == 'employer':
        instance.employerprofile.save()