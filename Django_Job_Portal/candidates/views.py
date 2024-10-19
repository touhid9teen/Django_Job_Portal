from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CandidateProfile
from .serializers import CandidateSerializer
from django.shortcuts import get_object_or_404


class CandidateListView(APIView):
    def post(self, request):
        serializer = CandidateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        try:
            user_profile = get_object_or_404(CandidateProfile, user=request.user)
            serializer = CandidateSerializer(user_profile, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except CandidateProfile.DoesNotExist:
            return Response({"error": "Profile not found"}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request):
        user_id = request.GET.get('user_id')

        if user_id:
            candidate_profile = get_object_or_404(CandidateProfile, id=user_id)
        else:
            candidate_profile = get_object_or_404(CandidateProfile, user=request.user)

        serializer = CandidateSerializer(candidate_profile)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CandidateDetailView(APIView):
    def get(self, request):
        candidates = CandidateProfile.objects.all()
        serializer = CandidateSerializer(candidates, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
