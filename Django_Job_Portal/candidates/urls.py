from django.urls import path

from candidates.views import CandidateListView, CandidateDetailView, CandidateJobApplicantListView

urlpatterns = [
    path('candidates/', CandidateListView.as_view(), name='candidate-list'),
    path('candidates-info/', CandidateDetailView.as_view(), name='candidate-detail'),
    path('candidate-application-list/', CandidateJobApplicantListView.as_view(), name='candidate-detail'),
]

# todo: candidate koto gula job apply korche setar jonno ekta api lagbe , pagination must---------------
# todo: jeto gula api list pagination apply---------------------------