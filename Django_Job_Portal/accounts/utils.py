from django.core.mail import send_mail
from django.conf import settings
import string
import random


def generate_otp():
    return ''.join(random.choice(string.digits) for _ in range(6))


def send_welcome_email(otp, email):
    try:
        subject = 'Your Account Verification email :'
        message = f'Your otp is {otp}'
        from_email = settings.EMAIL_HOST_USER
        to_email = [email]
        send_mail(subject, message, from_email, to_email)
    except Exception as e:
        print(f"Failed to send email: {str(e)}")
