from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
import string
import random
from datetime import timedelta
from django.utils import timezone
from job_portal.settings import SECRET_KEY
import jwt
import os
from dotenv import load_dotenv
load_dotenv()

def generate_otp():
    otp_length  = int(os.getenv('OTP_LENGTH',6))
    return ''.join(random.choice(string.digits) for _ in range(otp_length))

@shared_task
def send_welcome_email(otp, email):
    try:
        subject = 'Your Account Verification email :'
        message = f'Your otp is {otp}'
        from_email = settings.EMAIL_HOST_USER
        to_email = [email]
        send_mail(subject, message, from_email, to_email)
    except Exception as e:
        print(f"Failed to send email: {str(e)}")


def token_generation(user):
    uptime = timezone.now() + timedelta(minutes=30)
    print("token user", user, user.id, user.contract_number)
    payload = {
        'id': user.id,
        'email': user.email,
        'user_type': user.user_type,
        'contact_number': user.contract_number,
        'exp': uptime,
    }

    encoded_token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return encoded_token