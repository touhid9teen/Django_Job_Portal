from rest_framework import serializers
from .models import EmployerProfile


class EmployerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployerProfile
        fields = '__all__'