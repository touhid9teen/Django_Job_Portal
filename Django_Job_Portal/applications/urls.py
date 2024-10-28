from django.urls import path
from .views import CreateAndListApiview, JobApplicationStatusUpdateAPIView

urlpatterns = [
    path('job-application/<int:job_id>/', CreateAndListApiview.as_view(), name='application'),
    path('job-application-user/<int:application_id>/',
         JobApplicationStatusUpdateAPIView.as_view(),
         name='job-application'
         ),
]