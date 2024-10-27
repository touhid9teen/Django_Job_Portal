from django.urls import path
from .views import CreateAndListApiview, UpdateAndDeleteApiView

urlpatterns = [
    path('job-application/<int:job_id>', CreateAndListApiview.as_view(), name='application'),
    path('job-application-user/', UpdateAndDeleteApiView.as_view(), name='job-application'),
]