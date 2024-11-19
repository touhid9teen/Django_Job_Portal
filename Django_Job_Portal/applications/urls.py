from django.urls import path
from .views import CreateAndListApiview, JobApplicationStatusUpdateAPIView, AllJobApplicationDetailsView

urlpatterns = [
    path('<int:job_id>/', CreateAndListApiview.as_view(), name='application'),
    path('status/<int:application_id>/',
         JobApplicationStatusUpdateAPIView.as_view(),
         name='job-application-status'
         ),
    path('all/<int:job_id>/', AllJobApplicationDetailsView.as_view(), name='job-applications'),
]