# management/commands/generate_dummy_users.py
from django.core.management.base import BaseCommand
from accounts.factories import UserFactory
from accounts.models import Users

NUM_USERS = 5000

class Command(BaseCommand):
    help = "Generates dummy user data"

    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old user data...")
        Users.objects.all().delete()

        self.stdout.write("Creating new dummy users...")
        for _ in range(NUM_USERS):
            UserFactory()

        self.stdout.write(self.style.SUCCESS(f'Successfully created {NUM_USERS} dummy users.'))
