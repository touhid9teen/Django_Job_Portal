# management/commands/generate_dummy_jobs.py
import random
from django.core.management.base import BaseCommand
from django.db import transaction
from jobs.models import Job  # Adjust the import based on your app structure
from jobs.factories import JobFactory  # Adjust the import based on your app structure

NUM_JOBS = 50000  # Number of jobs to create

class Command(BaseCommand):
    help = "Generates dummy job entries"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old job data...")
        Job.objects.all().delete()  # Clear existing job entries

        self.stdout.write("Creating new job entries...")
        for _ in range(NUM_JOBS):
            job = JobFactory()
            self.stdout.write(f"Created job: {job.title} at {job.company_name}")
