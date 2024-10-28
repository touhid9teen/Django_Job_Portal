from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from accounts.authenticate import CustomAuthentication
from accounts.permissions import IsCandidate
from applications.models import JobApplication
from applications.serializers import JobApplicationSerializer
from .models import CandidateProfile
from .serializers import CandidateSerializer, CandidateSkillsSerializer
from django.shortcuts import get_object_or_404


class CandidateProfileUpdateAndGetView(APIView):
    authentication_classes = [CustomAuthentication]
    def post(self, request):
        serializer = CandidateSkillsSerializer(data=request.data)
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
        try:
            candidate_profile = CandidateProfile.objects.get(user=request.user)
            print("user",request.user)
            serializer = CandidateSerializer(candidate_profile)
            print("serializer", serializer.data)
            return Response(serializer.data)
        except CandidateProfile.DoesNotExist:
            return Response({"error": "Profile not found"}, status=status.HTTP_404_NOT_FOUND)



class AnyCandidateProfileView(APIView):
    authentication_classes = [CustomAuthentication]
    def get(self, request, candidate_id):
        try:
            candidate_profile = CandidateProfile.objects.get(id=candidate_id)
            serializer = CandidateSerializer(candidate_profile)
            return Response(serializer.data)
        except CandidateProfile.DoesNotExist:
            return Response({"error": "Profile not found"}, status=status.HTTP_404_NOT_FOUND)


class AllCandidateProfileView(APIView):
    authentication_classes = [CustomAuthentication]
    def get(self, request):
        try:
            candidates_profiles = CandidateProfile.objects.all()
            serializer = CandidateSerializer(candidates_profiles, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class CandidateJobApplicantListView(APIView):
    authentication_classes = [CustomAuthentication]
    permission_classes = [IsCandidate]
    def get(self, request):
        try:
            candidate_id = request.user.candidate.id
            total_application = JobApplication.objects.filter(candidate_id=candidate_id)
            serializer = JobApplicationSerializer(total_application, many=True)
            total_application = total_application.count()
            # todo: list er jonno serializer needed
            return Response({"Total_Application": total_application, "data" : serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)