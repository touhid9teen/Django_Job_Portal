from django.urls import path

from candidates.views import CandidateListView, CandidateDetailView

urlpatterns = [
    path('candidates/', CandidateListView.as_view(), name='candidate-list'),
    path('candidates-info/', CandidateDetailView.as_view(), name='candidate-detail'),
]