from django.urls import path
from . import views
urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('verify_otp/', views.ValidedOtpView.as_view(), name='otp_validate'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('user_info/', views.UserInfoView.as_view(), name='user_info'),

]
