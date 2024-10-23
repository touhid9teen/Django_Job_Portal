from django.dispatch import receiver,Signal
from .models import Users
from candidates.models import CandidateProfile
from employers.models import EmployerProfile

# todo: otp verified then signals apply
otp_verified = Signal()

@receiver(otp_verified)
def create_user_profile(sender, instance, **kwargs):
    if instance.user_type == 'candidate':
        CandidateProfile.objects.create(user=instance)
    elif instance.user_type == 'employer':
        EmployerProfile.objects.create(user=instance)