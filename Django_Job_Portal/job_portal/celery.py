import os
from celery import Celery
import accounts.utils


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'job_portal.settings')
app = Celery('job_portal')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()