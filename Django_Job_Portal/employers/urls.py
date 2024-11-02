from django.urls import path
from .views import EmployerListView, AllEmployerProfileView, AnyEmployerProfileView

urlpatterns = [
    path('employers/profile/', EmployerListView.as_view(), name='employer-list'),
    path('employer/profile/<int:employer_id>/', AnyEmployerProfileView.as_view(), name='any-employer-profile'),
    path('employers-info/', AllEmployerProfileView.as_view(), name='employer-detail'),
]