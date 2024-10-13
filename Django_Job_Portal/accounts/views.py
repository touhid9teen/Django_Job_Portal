from .models import Users
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from accounts.serializers import UserSerializer
from .utils import generate_otp, send_welcome_email


class UsersView(APIView):
    def get(self, request):
        try:
            users = Users.objects.all()
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response({'status': 'User created successfully'}, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            print("serilizer data", serializer.validated_data)
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
    def post(self, request):
        otp = request.data.get('otp')
        email = request.data.get('email')
        try:
            user = Users.objects.filter(otp=otp, email=email)

            if user.otp != otp:
                return Response({'status': 'Invalid OTP'}, status=status.HTTP_400_BAD_REQUEST)

            user.is_verified = True
            user.otp = False
            user.save()

            return Response({'status': 'Registation successfull'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class LoginView(APIView):
    def post(self, request):
        # Implement login logic here
        pass
