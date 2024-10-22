# management/commands/generate_dummy_employers.py
from django.core.management.base import BaseCommand
from django.db import transaction
from employers.factories import EmployerProfileFactory
from accounts.factories import UserFactory

NUM_EMPLOYERS = 1000  # Number of employer profiles to generate

class Command(BaseCommand):
    help = "Generates dummy employer profiles"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        from employers.models import EmployerProfile
        from accounts.models import Users

        EmployerProfile.objects.all().delete()
        Users.objects.all().delete()

        self.stdout.write("Creating new data...")
        # Generate the employer profiles
        for _ in range(NUM_EMPLOYERS):
            user = UserFactory(user_type='employer')  # Create a new user with 'employer' type
            EmployerProfileFactory(user=user)

        self.stdout.write(self.style.SUCCESS(f"Successfully created {NUM_EMPLOYERS} employer profiles."))

