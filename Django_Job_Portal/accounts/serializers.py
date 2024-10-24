from django.contrib.auth.password_validation import validate_password

from candidates.serializers import CandidateSerializer
from employers.serializers import EmployerProfileSerializer
from .models import Users
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'email', 'contract_number', 'user_type', 'password']


class CandidateDetailsProfileSerializer(serializers.ModelSerializer):
    candidate = CandidateSerializer(read_only=True)
    class Meta:
        model = Users
        fields = '__all__'
        # fields = ['candidate_profile', 'id', 'email', 'contract_number', 'user_type', 'password']

class EmployerDetailsProfileSerializer(serializers.ModelSerializer):
    employer = EmployerProfileSerializer(read_only=True)
    class Meta:
        model = Users
        fields = '__all__'

class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    confirm_password = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = Users
        fields = ['password', 'confirm_password', 'old_password']

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError({'password': 'Password field does not match'})
        return data

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError({'old_password': 'Old password is incorrect'})
        return value

    def update(self, instance, validated_data):

        instance.set_password(validated_data['password'])
        instance.save()
        return instance