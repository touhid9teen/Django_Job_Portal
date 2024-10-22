# factories.py
import factory
from factory.django import DjangoModelFactory
from faker import Faker
from accounts.factories import UserFactory
from employers.models import EmployerProfile  # Import the EmployerProfile model

fake = Faker()

class EmployerProfileFactory(DjangoModelFactory):
    class Meta:
        model = EmployerProfile

    user = factory.SubFactory(UserFactory)  # Use the UserFactory to create an associated user
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    address = factory.Faker('address')
    website = factory.Faker('url')
    company_name = factory.Faker('company')
    profile_picture = None  # Optionally, leave the profile picture field as None for now

    # You can further customize fields if needed
