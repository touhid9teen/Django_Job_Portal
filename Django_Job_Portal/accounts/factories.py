# factories.py
import factory
from factory.django import DjangoModelFactory
from faker import Faker
from .models import Users

fake = Faker()

class  UserFactory(DjangoModelFactory):
    class Meta:
        model = Users

    email = factory.Sequence(lambda n: f'user{n}@example.com')
    contract_number = factory.LazyAttribute(lambda _: fake.phone_number())
    user_type = factory.Iterator(['candidate', 'employer'])
    password = factory.PostGenerationMethodCall('set_password', '1234')
    is_verified = True
    otp = None

    # Optional: You can customize the creation of each instance further if needed
    @factory.post_generation
    def set_username(self, create, extracted, **kwargs):
        self.username = self.email.split('@')[0]
        if create:
            self.save()
