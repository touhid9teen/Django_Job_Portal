from rest_framework import serializers
from .models import Job

class JobSerializer(serializers.ModelSerializer):
    # Todo: individual jobs e total candidate applied
    class Meta:
        model = Job
        fields = '__all__'