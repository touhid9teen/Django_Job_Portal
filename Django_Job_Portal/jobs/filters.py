from django_filters import rest_framework as filters
from .models import Job

class JobFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')
    job_type = filters.ChoiceFilter(choices=Job.TYPE_CHOICES)
    job_subtype = filters.ChoiceFilter(choices=Job.SUBTYPE_CHOICES)
    experience_level = filters.ChoiceFilter(choices=Job.EXPERIENCE_LEVEL_CHOICES)
    location = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Job
        fields = ['title', 'job_type', 'job_subtype', 'experience_level', 'location']