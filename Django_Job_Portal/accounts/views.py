
from .models import Users
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from accounts.serializers import UserSerializer
from .utils import generate_otp, send_welcome_email
from .authenticate import CustomAuthentication
from .utils import token_generation
from django.contrib.auth import authenticate
from .utils import token_generation


class RegisterView(APIView):
    authentication_classes = []
    def post(self, request):
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
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ValidedOtpView(APIView):
    authentication_classes = []
    def post(self, request):
        otp = request.data.get('otp')
        email = request.data.get('email')
        try:
            user = Users.objects.get(otp=otp)

            if user.otp != otp:
                return Response({'status': 'Invalid OTP'}, status=status.HTTP_400_BAD_REQUEST)
            if user.email != email:
                return Response({'status': 'Invalid Email'}, status=status.HTTP_400_BAD_REQUEST)

            user.is_verified = True
            user.otp = None
            user.save()

            return Response({'status': 'Registation successfull'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class LoginView(APIView):
    authentication_classes = []
    def post(self, request):
        identifier = request.data.get('email_or_phone')
        password = request.data.get('password')

        if not identifier or not password:
            return Response({'error': 'Please provide both email and password'}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(request, username=identifier, password=password)
        print(user)
        if user is None:
            return Response({'error': 'Invalid email or phone number or password.'},status=status.HTTP_401_UNAUTHORIZED)

        try:
            token = token_generation(user)
            return Response({'access token': str(token)}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': f'Token generation failed: {str(e)}'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UserInfoView(APIView):
    authentication_classes = [CustomAuthentication]
    def get(self, request):

        total_user = Users.objects.count()
        users = Users.objects.all()
        serializer = UserSerializer(users, many=True)

        return Response({'Total User' : total_user, 'Users' : serializer.data}, status=status.HTTP_200_OK)
