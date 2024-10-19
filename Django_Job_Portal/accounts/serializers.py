from .models import Users
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'email', 'contract_number', 'user_type', 'password']
