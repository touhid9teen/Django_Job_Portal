from django.urls import path
from .views import EmployerListView, EmployerDetailView

urlpatterns = [
    path('employers/', EmployerListView.as_view(), name='employer-list'),
    path('employers-info/', EmployerDetailView.as_view(), name='employer-detail'),
]