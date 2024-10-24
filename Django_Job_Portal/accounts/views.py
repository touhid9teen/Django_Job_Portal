from .models import Users
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from accounts.serializers import UserSerializer
from .utils import generate_otp, send_welcome_email, token_generation
from .authenticate import CustomAuthentication
from django.contrib.auth import authenticate


class RegisterView(APIView):
    authentication_classes = []

    def post(self, request):
        try:
            email = request.data['email']
            phone = request.data['contract_number']

            existing_with_email = Users.objects.filter(email=email)
            users_with_phone = Users.objects.filter(contract_number=phone)

            if users_with_phone and existing_with_email:
                return Response({'error': 'Email and Phone already in use.'}, status=status.HTTP_400_BAD_REQUEST)

            if existing_with_email.exists():
                return Response({'error': 'Email already in use.'}, status=status.HTTP_400_BAD_REQUEST)

            if users_with_phone.exists():
                return Response({'error': 'Phone number already in use.'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            try:
                validated_data = serializer.validated_data
                user = Users.objects.create_user(**validated_data)
                otp = generate_otp()
                user.otp = otp
                user.save()
                send_welcome_email(otp, user.email)
                return Response({'status': 'OTP has been generated', 'otp': otp}, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({'error': f"User registration failed: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ValidedOtpView(APIView):
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
            total_user = Users.objects.count()
            users = Users.objects.all()
            serializer = UserSerializer(users, many=True)

            return Response({'Total User': total_user, 'Users': serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': f"Failed to retrieve users: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
