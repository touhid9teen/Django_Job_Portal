from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.core.validators import validate_email, EmailValidator
from candidates.models import CandidateProfile
from candidates.serializers import CandidateSerializer
from employers.models import EmployerProfile
from employers.serializers import EmployerProfileSerializer
from .models import Users
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = Users
        fields = ['id', 'email', 'contract_number', 'user_type', 'password']
        extra_kwargs = {
            'email': {'write_only': True, 'required': True},
            'contract_number': {'write_only': True, 'required': True}
        }

    def validate(self, attrs):
        email = attrs.get('email')
        contract_number = attrs.get('contract_number')

        # Validate email
        if Users.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email': 'Email already registered'})
        validate_email(email)

        # Validate and normalize contract number
        contract_number = contract_number.strip()
        if contract_number.startswith('+'):
            contract_number = contract_number[3:]
        if len(contract_number) == 13:
            contract_number = contract_number[2:]
        if not contract_number.isdigit() or len(contract_number) != 11:
            raise serializers.ValidationError({
                'contract_number': 'Contract number must contain 11 digits (e.g., 01XXXXXXXXX).'
            })
        if Users.objects.filter(contract_number=contract_number).exists():
            raise serializers.ValidationError({'contract_number': 'Contract number is already registered.'})

        # Update attributes for further processing
        attrs['contract_number'] = contract_number
        return attrs

    def create(self, validated_data):
        # Use the validated data to create the user
        return Users.objects.create_user(**validated_data)




class LoginSerializer(serializers.Serializer):
    email_or_phone = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True)

    def validate_identifier(self, value):
        email_validator = EmailValidator()
        try:
            email_validator(value)
            self.context['is_email'] = True
        except ValidationError:
            if value.isdigit() and len(value) == 11:
                self.context['is_phone'] = True
            else:
                raise serializers.ValidationError(_("Enter a valid email or phone number."))

        return value

    def validate(self, data):
        email_or_phone = data.get('email_or_phone')
        password = data.get('password')

        # Determine if identifier is email or phone
        auth_kwargs = {'username': email_or_phone, 'password': password}
        if self.context.get('is_phone'):
            auth_kwargs = {'phone': email_or_phone, 'password': password}

        user = authenticate(**auth_kwargs)
        print("user", user)
        if user is None:
            raise serializers.ValidationError(_("Invalid email/phone or password."))

        if not user.is_verified:
            raise serializers.ValidationError(_("Please verify your account via OTP."))

        data['user'] = user
        return data


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

class OtpVerificationSerializer(serializers.Serializer):
    otp = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)

    def validate_otp(self, otp):
        if len(otp) != 6 or not otp.isdigit():
            raise serializers.ValidationError('OTP must be a 6-digit numeric value.')

        if not Users.objects.filter(otp=otp).exists():
            raise serializers.ValidationError('OTP does not exist.')

        return otp

    def validate_email(self, email):
        if not Users.objects.filter(email=email).exists():
            raise serializers.ValidationError('Email does not exist.')
        return email


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


class ModelSerializer:
    pass