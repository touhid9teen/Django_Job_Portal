from django.db.models import Q
from rest_framework.pagination import PageNumberPagination
from .models import Users
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from accounts.serializers import UserSerializer, ChangePasswordSerializer, CandidateDetailsProfileSerializer,EmployerDetailsProfileSerializer, UserDetailsProfileSerializer, OtpVerificationSerializer, LoginSerializer
from .utils import send_welcome_email, token_generation
from .authenticate import CustomAuthentication
from django.contrib.auth import authenticate
from .signals import otp_verified


class RegisterView(APIView):
    authentication_classes = []

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            try:
                user = serializer.save()
                send_welcome_email.delay(user.otp, user.email)
                return Response({'status': 'OTP has been generated', 'otp': user.otp}, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({'error': f"User registration failed: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ValidatedOtpView(APIView):
    authentication_classes = []

    def post(self, request):
        try:
            serializer = OtpVerificationSerializer(data=request.data, context = {'request': request})

            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            user = Users.objects.filter(email=serializer.data['email'], otp=serializer.data['otp']).first()

            if not user:
                return Response({'error': 'Invalid OTP or email combination'}, status=status.HTTP_400_BAD_REQUEST)

            user.is_verified = True
            user.save()
            otp_verified.send(sender=user.__class__, instance=user)

            return Response({'status': 'Registration successful'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': f"OTP validation failed: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class LoginView(APIView):
    authentication_classes = []

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        print("data", request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = Users.objects.get(Q(email=serializer.data['email_or_phone']) | Q(contract_number=serializer.data['email_or_phone']))
            token = token_generation(user)
            return Response({'access_token': str(token)}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': f"Token generation failed: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class UserInfoView(APIView):
    authentication_classes = [CustomAuthentication]

    def get(self, request):
        try:
            users = Users.objects.all()
            pageinator = PageNumberPagination()
            pageinator.page_size = 10
            pageinatorquery = pageinator.paginate_queryset(users, request)
            serializer = UserDetailsProfileSerializer(pageinatorquery, many=True)
            return pageinator.get_paginated_response(serializer.data)
        except Exception as e:
            return Response({'error': f"Failed to retrieve users: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ChangePasswordView(APIView):
    authentication_classes = [CustomAuthentication]
    def patch(self, request):
        serializer = ChangePasswordSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            user = request.user
            serializer.update(user, serializer.validated_data)
            return Response({'detail':'Password Change Successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginUserProfileView(APIView):
    authentication_classes = [CustomAuthentication]
    def get(self, request):
        try:
            user = Users.objects.get(id=request.user.id)
            if request.user.user_type == 'candidate':
                serializer = CandidateDetailsProfileSerializer(user)
            elif request.user.user_type == 'employer':
                serializer = EmployerDetailsProfileSerializer(user)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)

class LogoutView(APIView):
    authentication_classes = [CustomAuthentication]
    def post(self, request):
        pass