from django.urls import path
from .views import (
    CreateAndListApiview,
    UpdateAndDeleteApiView,
    JobFilterView
)

urlpatterns = {
    path('jobs/manage/', CreateAndListApiview.as_view(), name='job_manage'),
    path('jobs/manage/<int:job_id>/', UpdateAndDeleteApiView.as_view(), name='job_manage_by_id'),
    path('jobs/search/', JobFilterView.as_view(), name='job_search'),
}