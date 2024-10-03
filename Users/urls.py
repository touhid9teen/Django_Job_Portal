from django.urls import path
from . import views
urlpatterns = [
    path('register/', views.RegisterView, name='index'),
    path('Verify_otp/', views.ValidedOtpView, name='otp_validate'),
]