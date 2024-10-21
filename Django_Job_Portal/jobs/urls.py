from django.urls import path
from .views import JobListView, JobPostView

urlpatterns = {
    path('jobs/', JobListView.as_view(), name='job_list'),
    path('jobs-post/', JobPostView.as_view(), name='job_post'),
}