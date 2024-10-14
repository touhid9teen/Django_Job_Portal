from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class Users(AbstractUser):

    USER_TYPES = (
        ('candidate', 'Candidate'),
        ('employer', 'Employer'),
        ('admin', 'Admin'),
    )
    username = models.CharField()
    email = models.EmailField(unique=True)
    contract_number = models.CharField(max_length=50)
    user_type = models.CharField(max_length=10, choices=USER_TYPES)
    password = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)
    otp = models.CharField(max_length=8, null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['contract_number', 'user_type']

    def __str__(self):
        return self.email
