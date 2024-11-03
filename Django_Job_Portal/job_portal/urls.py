from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('candidate/', include('candidates.urls')),
    path('employer/', include('employers.urls')),
    path('job/', include('jobs.urls')),
    path('application/', include('applications.urls')),
]

# admin.site.site_header = "Job Portal"
# admin.site.site_title = "Job Portal"
