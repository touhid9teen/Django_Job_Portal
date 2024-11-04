from django.urls import path

from candidates.views import CandidateJobApplicantListView, CandidateProfileUpdateAndGetView, AnyCandidateProfileView,AllCandidateProfileView

urlpatterns = [
    path('profile/', CandidateProfileUpdateAndGetView.as_view(), name='candidate-profile'),
    path('profile/<int:candidate_id>/', AnyCandidateProfileView.as_view(), name='candidate-profile-view   '),
    path('profiles/', AllCandidateProfileView.as_view(), name='candidate-profiles'),
    path('application/list/', CandidateJobApplicantListView.as_view(), name='candidate-job-application-list'),
]

