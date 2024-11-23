from django.urls import path
from .views import EmployerStatusAndUpdateView, AllEmployerProfileView, AnyEmployerProfileView

urlpatterns = [
    path('profile/', EmployerStatusAndUpdateView.as_view(), name='employer-list'),
    path('profile/<int:employer_id>/', AnyEmployerProfileView.as_view(), name='any-employer-profile'),
    path('profiles/', AllEmployerProfileView.as_view(), name='employer-detail'),
]