from django.core.management.base import BaseCommand
from jobs.factories import JobFactory  # Import your JobFactory
from jobs.models import Job  # Import your Job model

NUM_JOBS = 0  # Set the number of jobs you want to create

class Command(BaseCommand):
    help = "Generates dummy job data"

    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old job data...")

        # Delete all existing job data
        Job.objects.all().delete()

        self.stdout.write("Creating new dummy jobs...")

        # Create new dummy jobs using JobFactory
        for _ in range(NUM_JOBS):
            JobFactory()

        self.stdout.write(self.style.SUCCESS(f'Successfully created {NUM_JOBS} dummy jobs.'))
