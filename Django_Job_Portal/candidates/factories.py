# factories.py
import factory
from factory.django import DjangoModelFactory
from faker import Faker
from .models import CandidateProfile
from accounts.factories import UserFactory  # Assuming you have UserFactory already defined

fake = Faker()

class CandidateProfileFactory(DjangoModelFactory):
    class Meta:
        model = CandidateProfile

    user = factory.SubFactory(UserFactory)
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    address = factory.Faker('address')
    resume = None  # Leave as None to avoid file uploads
    profile_pic = None  # Leave as None to avoid file uploads

    bio = factory.Faker('text')
    education = factory.Faker('sentence', nb_words=5)
    experience = factory.Faker('paragraph')
    skills = factory.List([fake.word() for _ in range(5)])  # Generating a list of 5 random skills
    social_links = factory.List([fake.url() for _ in range(3)])  # Generating a list of 3 random URLs

    # Optional post-generation processing for custom handling if needed
    @factory.post_generation
    def set_user(self, create, extracted, **kwargs):
        if create:
            self.save()
