from django.urls import path
from .views import CreateAndListApiview, JobApplicationStatusUpdateAPIView, AllJobApplicationDetailsView

urlpatterns = [
    path('application/<int:job_id>/', CreateAndListApiview.as_view(), name='application'),
    path('application-user/<int:application_id>/',
         JobApplicationStatusUpdateAPIView.as_view(),
         name='job-application'
         ),
    path('all/application/<int:job_id>/', AllJobApplicationDetailsView.as_view(), name='job-application-status'),
]