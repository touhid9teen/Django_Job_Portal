from django.core.serializers import serialize
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CandidateProfile
from .serializers import CandidateSerializer


class CandidateListView(APIView):
    def post(self, request):
        serialize = CandidateSerializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status=status.HTTP_201_CREATED)
        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        user_profile = CandidateProfile.objects.get(user=request.user)
        serializer = CandidateSerializer(user_profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        user_id = request.GET.get('user_id')

        if user_id:
            try:
                candidates = CandidateProfile.objects.get(id=user_id)
                serializer = CandidateSerializer(candidates)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except CandidateProfile.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            try:
                candidates = CandidateProfile.objects.get(user=request.user)
                serializer = CandidateSerializer(candidates)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except CandidateProfile.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

class CandidateDetailView(APIView):
    def get(self, request):
        try:
            candidates = CandidateProfile.objects.all()
            serializer = CandidateSerializer(candidates, many=True)
            return Response(serializer.data)
        except CandidateProfile.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)