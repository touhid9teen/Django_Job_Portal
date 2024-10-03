from django.core.mail import send_mail
from django.conf import settings
import string
import random

def generate_otp():
    characters = string.digits
    otp = ''.join(random.choice(characters) for _ in range(8))
    return otp

def send_welcome_email(otp, email):
    subject = 'Your OTP is :'
    message = f'{otp}'
    from_email = settings.EMAIL_HOST_USER
    to_email = email
    send_mail(subject, message, from_email, to_email)
