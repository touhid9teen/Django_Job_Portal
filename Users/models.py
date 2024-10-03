from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, password, conform_password, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')


        if password != conform_password:
            raise ValueError('Passwords does not match')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save()
        return user


class Users(AbstractUser):

    user_choose_type = (
        ('candidate', 'Candidate'),
        ('employer',  'Employer'),
    )

    email = models.EmailField(unique=True)
    contract_number = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    conform_password = models.CharField(max_length=50)
    user_type = models.CharField(max_length=50, choices=())
    otp = models.CharField(max_length=8, null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['contract_number', 'password', 'user_type', 'email', 'conform_password']
