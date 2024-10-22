import factory
from factory.django import DjangoModelFactory
from faker import Faker
from .models import JobApplication
from jobs.models import Job
from candidates.models import CandidateProfile
from accounts.models import Users
from jobs.factories import JobFactory
from candidates.factories import CandidateProfileFactory
from accounts.factories import UserFactory


fake = Faker()

class JobApplicationFactory(DjangoModelFactory):
    class Meta:
        model = JobApplication

    job = factory.SubFactory(JobFactory)  # Generate a Job instance
    candidate = factory.SubFactory(CandidateProfileFactory)  # Generate a CandidateProfile instance
    user = factory.SubFactory(UserFactory)  # Generate a Users instance
    application_date = factory.LazyFunction(fake.date_time)
    email = factory.Sequence(lambda n: f'user{n}@example.com')
    status = factory.Iterator([choice[0] for choice in JobApplication.STATUS_CHOICES])
    cover_letter = factory.LazyAttribute(lambda _: fake.paragraph(nb_sentences=3))
    resume = factory.LazyAttribute(lambda _: fake.file_name(category='document', extension='pdf'))
