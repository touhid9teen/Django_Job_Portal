from django.core.serializers import serialize
from rest_framework.pagination import PageNumberPagination
from .models import Users
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from accounts.serializers import UserSerializer, ChangePasswordSerializer, CandidateDetailsProfileSerializer, EmployerDetailsProfileSerializer, UserDetailsProfileSerializer
from .utils import generate_otp, send_welcome_email, token_generation
from .authenticate import CustomAuthentication
from django.contrib.auth import authenticate
from .signals import otp_verified


class RegisterView(APIView):
    authentication_classes = []

    def post(self, request):

        email = request.data['email']
        phone = request.data['contract_number']

            # todo: validation everything convert serializer validation and phone number validation
            # todo: 8 length password validation

        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            try:
                validated_data = serializer.validated_data
                user = Users.objects.create_user(**validated_data)
                print("validated_data",validated_data, user)
                # todo: save override kaj koro
                otp = generate_otp()
                print("otp",otp)
                user.otp = otp

                user.save()

                send_welcome_email.delay(otp, user.email)
                return Response({'status': 'OTP has been generated', 'otp': otp}, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({'error': f"User registration failed: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ValidatedOtpView(APIView):
    authentication_classes = []

    def post(self, request):
        otp = request.data.get('otp')
        email = request.data.get('email')

        if not otp or not email:
            return Response({'error': 'Both OTP and email are required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = Users.objects.filter(otp=otp).first()
            if not user or user.email != email:
                return Response({'status': 'Invalid OTP or Email'}, status=status.HTTP_400_BAD_REQUEST)

            user.is_verified = True
            user.otp = None
            user.save()

            otp_verified.send(sender=user.__class__, instance=user)

            return Response({'status': 'Registration successful'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': f"OTP validation failed: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class LoginView(APIView):
    authentication_classes = []

    def post(self, request):
        identifier = request.data.get('email_or_phone')
        password = request.data.get('password')

        # Validate the presence of both identifier and password
        if not identifier or not password:
            return Response({'error': 'Please provide both email/phone and password'}, status=status.HTTP_400_BAD_REQUEST)

        # Authenticate the user
        user = authenticate(request, username=identifier, password=password)

        # If user authentication fails
        if user is None:
            return Response({'error': 'Invalid email/phone or password.'}, status=status.HTTP_401_UNAUTHORIZED)

        # Check if the user is verified
        if not user.is_verified:
            return Response({'error': 'Please verify your account via OTP.'}, status=status.HTTP_400_BAD_REQUEST)

        # Generate token if authentication and verification are successful
        try:
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