from django.urls import path

from candidates.views import CandidateJobApplicantListView, CandidateProfileUpdateAndGetView, AnyCandidateProfileView,AllCandidateProfileView

urlpatterns = [
    path('candidates/profile/', CandidateProfileUpdateAndGetView.as_view(), name='candidate-profile'),
    path('candidates/profile/<int:candidate_id>/', AnyCandidateProfileView.as_view(), name='candidate-profile-view   '),
    path('candidate/profiles/', AllCandidateProfileView.as_view(), name='candidate-profiles'),
    path('candidate/application/list/', CandidateJobApplicantListView.as_view(), name='candidate-job-application-list'),
]

# todo: candidate koto gula job apply korche setar jonno ekta api lagbe , pagination must---------------
# todo: jeto gula api list pagination apply---------------------------