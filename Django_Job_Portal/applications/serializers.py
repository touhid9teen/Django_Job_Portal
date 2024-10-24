from rest_framework import serializers

from candidates.serializers import CandidateSerializer
from jobs.serializers import JobSerializer
from .models import JobApplication

class JobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplication
        fields = '__all__'

# class JobApplicationCandidateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = JobApplication
#         fields = '__all__'

class JobApplicationCandidateDetailsSerializer(serializers.ModelSerializer):
    job = JobSerializer(read_only=True)
    candidate = CandidateSerializer(read_only=True)
    class Meta:
        model = JobApplication
        fields = '__all__'

