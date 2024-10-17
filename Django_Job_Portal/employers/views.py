from django.core.serializers import serialize
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import EmployerProfile
from .serializers import EmployerProfileSerializer


class EmployerListView(APIView):
    def post(self, request):
        serialize = EmployerProfileSerializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status=status.HTTP_201_CREATED)
        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        user_profile = EmployerProfile.objects.get(user=request.user)
        serializer = EmployerProfileSerializer(user_profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        user_id = request.GET.get('user_id')

        if user_id:
            try:
                candidates = EmployerProfile.objects.get(id=user_id)
                serializer = EmployerProfileSerializer(candidates)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except EmployerProfile.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            try:
                candidates = EmployerProfile.objects.get(user=request.user)
                serializer = EmployerProfileSerializer(candidates)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except EmployerProfile.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

class EmployerDetailView(APIView):
    def get(self, request):
        try:
            candidates = EmployerProfile.objects.all()
            serializer = EmployerProfileSerializer(candidates, many=True)
            return Response(serializer.data)
        except EmployerProfile.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)