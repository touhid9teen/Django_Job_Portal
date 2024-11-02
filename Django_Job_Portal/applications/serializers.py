from rest_framework import serializers

from candidates.serializers import CandidateSerializer
from employers.models import EmployerProfile
from jobs.serializers import JobSerializer
from .models import JobApplication
from jobs.models import Job

class JobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplication
        fields = '__all__'


class JobApplicationCandidateDetailsSerializer(serializers.ModelSerializer):
    job = JobSerializer(read_only=True)
    candidate = CandidateSerializer(read_only=True)
    # employer = serializers.SerializerMethodField(method_name='get_employer')

    class Meta:
        model = JobApplication
        fields = '__all__'

    # def get_employer(self, obj):
    #     employer = obj.job.employer
    #     return EmployerProfile.objects.get(employer).data