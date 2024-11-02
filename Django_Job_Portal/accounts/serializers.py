from django.contrib.auth.password_validation import validate_password
from django.core.validators import validate_email

from candidates.models import CandidateProfile
from candidates.serializers import CandidateSerializer
from employers.models import EmployerProfile
from employers.serializers import EmployerProfileSerializer
from .models import Users
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    class Meta:
        model = Users
        fields = ['id', 'email', 'contract_number', 'user_type', 'password']
        extra_kwargs = {
            'email': {'write_only': True, 'required': True},
            'contract_number': {'write_only': True, 'required': True}
        }

    def validate_email(self, email):
        if Users.objects.filter(email=email).exists():
            raise serializers.ValidationError('Email already registered')
        validate_email(email)
        return email

    def validate_contract_number(self, contract_number):
        contract_number = contract_number.strip()

        if contract_number.startswith('+'):
            country_code_length = 3
            digits_part = contract_number[1:]
            local_number_part = contract_number[country_code_length:]

            if not digits_part.isdigit() or len(digits_part) != 13:
                raise serializers.ValidationError(
                    'Contract number must contain 13 digits when using a country code (e.g., +88XXXXXXXXXXX).'
                )
        else:
            local_number_part = contract_number
            if not contract_number.isdigit() or len(contract_number) != 11:
                raise serializers.ValidationError(
                    'Contract number must be 11 digits for a local number.'
                )

        if Users.objects.filter(contract_number__in=[contract_number, local_number_part]).exists():
            raise serializers.ValidationError('Contract number is already registered.')

        return contract_number


class CandidateDetailsProfileSerializer(serializers.ModelSerializer):
    candidate = CandidateSerializer(read_only=True)
    class Meta:
        model = Users
        fields = ['id', 'email', 'contract_number', 'user_type', 'candidate']

class EmployerDetailsProfileSerializer(serializers.ModelSerializer):
    employer = EmployerProfileSerializer(read_only=True)
    class Meta:
        model = Users
        fields = ['id', 'email', 'contract_number', 'user_type', 'employer']

class UserDetailsProfileSerializer(serializers.ModelSerializer):
    user_details = serializers.SerializerMethodField()
    class Meta:
        model = Users
        fields = ['id', 'email', 'contract_number', 'user_type', 'user_details']

    def get_user_details(self, obj):
        if obj.user_type == 'candidate':
            candidateProfile = CandidateProfile.objects.filter(user=obj).first()
            if candidateProfile:
                return CandidateDetailsProfileSerializer(candidateProfile).data

        elif obj.user_type == 'employer':
            employerProfile = EmployerProfile.objects.filter(user=obj).first()
            if employerProfile:
                return EmployerDetailsProfileSerializer(employerProfile).data

        return None

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