from rest_framework import serializers

from employers.serializers import EmployerProfileSerializer
from .models import Job

class JobSerializer(serializers.ModelSerializer):
    # Todo: individual jobs e total candidate applied-----------------
    # job created employer details
    employer = EmployerProfileSerializer(read_only=True)
    class Meta:
        model = Job
        fields = '__all__'

    # to_representation jobs e total candidate applied