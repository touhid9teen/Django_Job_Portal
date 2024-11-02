from rest_framework import serializers

from applications.models import JobApplication
from employers.serializers import EmployerProfileSerializer
from .models import Job

class JobCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'


class JobSerializer(serializers.ModelSerializer):
    employer = EmployerProfileSerializer(read_only=True)
    class Meta:
        model = Job
        fields = '__all__'

class JobDetailSerializer(serializers.ModelSerializer):
    employer = EmployerProfileSerializer(read_only=True)
    total_applications = serializers.SerializerMethodField(method_name='get_total_applications')

    class Meta:
        model = Job
        fields = '__all__'

    def get_total_applications(self, obj):
        return JobApplication.objects.filter(job_id=obj.id).count()
    # to_representation jobs e total candidate applied