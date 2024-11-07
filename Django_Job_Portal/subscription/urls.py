from django.urls import path
from . import views

urlpatterns = [
    path('plan/', views.MakeSubscriptionView.as_view(), name='subscription_plan '),
    path('add/plan/', views.ChosenSubscriptionView.as_view(), name='subscription'),
]