from django.urls import path
from .views import JobApplicationView, JobApplicationListView

urlpatterns = [
    path('job-application/', JobApplicationView.as_view(), name='application'),
    path('job-application-user/', JobApplicationListView.as_view(), name='job-application'),
]