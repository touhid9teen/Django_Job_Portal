from django.urls import path
from . import views
urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('verify_otp/', views.ValidedOtpView.as_view(), name='otp_validate'),
]
