import os
from celery import Celery
import accounts.utils


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'job_portal.settings')
app = Celery('job_portal')
app.config_from_object('django.conf:settings', namespace='CELERY')
<<<<<<< HEAD

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

=======
app.autodiscover_tasks()
>>>>>>> 92fa7f7b939d4641d4b5a5f3515b3524acbf3b77
