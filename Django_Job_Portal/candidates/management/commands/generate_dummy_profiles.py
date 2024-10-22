# management/commands/generate_dummy_profiles.py
import random
from django.core.management.base import BaseCommand
from django.db import transaction
from accounts.factories import UserFactory
from candidates.factories import CandidateProfileFactory

NUM_PROFILES = 1000

class Command(BaseCommand):
    help = "Generates dummy candidate profiles"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        # Deleting old data to avoid duplication
        from candidates.models import CandidateProfile
        from accounts.models import Users

        CandidateProfile.objects.all().delete()
        Users.objects.all().delete()

        self.stdout.write("Creating new data...")
        # Generate candidate profiles
        for _ in range(NUM_PROFILES):
            user = UserFactory()  # Create a new user
            CandidateProfileFactory(user=user)  # Create a CandidateProfile associated with the user

        self.stdout.write(self.style.SUCCESS(f"Successfully created {NUM_PROFILES} candidate profiles."))
