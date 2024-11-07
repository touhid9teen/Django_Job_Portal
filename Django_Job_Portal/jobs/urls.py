from django.urls import path
from .views import (
    CreateAndListApiview,
    UpdateAndDeleteApiView,
    JobFilterView
)

urlpatterns = {
    path('manage/', CreateAndListApiview.as_view(), name='job_manage'),
    path('manage/<int:job_id>', UpdateAndDeleteApiView.as_view(), name='job_manage_by_id'),
    path('search/', JobFilterView.as_view(), name='job_search'),
}