from dulwich.porcelain import status
from requests import Response
from rest_framework.authtoken.admin import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Users.serializers import UserSerializer
from .utils import generate_otp, send_welcome_email


class UsersView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            otp = generate_otp()
            user = User.objects.get(email = request.user.email)
            user.otp = otp
            user.save()
            send_welcome_email(otp, request.user.email)
            return Response({'status' :'OTP has been sent to your mail'}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class ValidedOtpView(APIView):
    def get(self, request):
        email = request.user.email
        otp = request.user.otp
        user_otp = User.objects.filter(email=email, otp=otp)

        if user_otp != otp:
            return Response({'status' :'OTP does not match'}, status = status.HTTP_400_BAD_REQUEST)
        return Response({'status' :'OTP matches'}, status = status.HTTP_200_OK)



class LoginView(APIView):
    def post(self, request):
        pass
