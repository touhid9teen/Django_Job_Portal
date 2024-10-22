import factory
from factory.django import DjangoModelFactory
from faker import Faker
from .models import Job
from django.utils import timezone
from datetime import timedelta

fake = Faker()

class JobFactory(DjangoModelFactory):
    class Meta:
        model = Job

    title = factory.Faker('job')
    description = factory.Faker('paragraph')
    job_type = factory.Iterator(['Government', 'Private'])
    job_subtype = factory.Iterator(['Full-time', 'Part-time', 'Contract', 'Internship', 'Temporary', 'Freelance'])
    experience_level = factory.Iterator(['Entry', 'Mid', 'Senior', 'Director', 'Executive'])
    company_name = factory.Faker('company')
    location = factory.Faker('city')
    salary_range = factory.Faker('currency', locale='en_US')
    posted_at = factory.LazyFunction(timezone.now)
    deadline = factory.LazyAttribute(lambda _: fake.date_time_between(start_date=timezone.now(), end_date=timezone.now() + timedelta(days=30)))
    application_link = factory.Faker('url')
    application_email = factory.Faker('email')
    is_deleted = factory.Faker('boolean')
