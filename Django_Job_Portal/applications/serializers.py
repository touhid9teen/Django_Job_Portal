from rest_framework import serializers
from .models import JobApplication

class JobApplicationSerializer(serializers.ModelSerializer):
    # TODO: CANDIDATE DETAILS
    class Meta:
        model = JobApplication
        fields = '__all__'