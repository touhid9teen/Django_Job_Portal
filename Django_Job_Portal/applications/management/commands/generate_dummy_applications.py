# management/commands/generate_dummy_applications.py
from django.core.management.base import BaseCommand
from django.db import transaction
from applications.models import JobApplication  # Adjust the import based on your app structure
from applications.factories import JobApplicationFactory  # Adjust the import based on your app structure

NUM_APPLICATIONS = 200  # Number of applications to create

class Command(BaseCommand):
    help = "Generates dummy job application entries"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old application data...")
        JobApplication.objects.all().delete()  # Clear existing applications

        self.stdout.write("Creating new job application entries...")
        for _ in range(NUM_APPLICATIONS):
            application = JobApplicationFactory()
            self.stdout.write(f"Created application for job: {application.job.title} by user: {application.user.email}")
