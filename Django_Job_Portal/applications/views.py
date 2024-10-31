from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.core.cache import cache
from accounts.authenticate import CustomAuthentication
from accounts.permissions import IsCandidate, IsEmployer
from jobs.models import Job
from .models import JobApplication
from .serializers import (
    JobApplicationSerializer,
    JobApplicationCandidateDetailsSerializer
)

# my_cache_key = "upay_cache_key"
class  CreateAndListApiview(APIView):
    authentication_classes = [CustomAuthentication]
    permission_classes = [IsCandidate]
    def post(self, request, job_id):
        # my_dinamic_cache_key = my_cache_key+str(job_id)

        is_applied = JobApplication.objects.filter(candidate__user__id=request.user.id, job=job_id).exists()

        if is_applied:
            return Response({'status': 'Already Applied'}, status=status.HTTP_200_OK)
        serializer = JobApplicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class AllJobApplicationDetailsView(APIView):
    authentication_classes = [CustomAuthentication]
    permission_classes = [IsEmployer]
    def get(self, request, job_id):
        try:
            job_applications = JobApplication.objects.filter(job_id=job_id)
            job = Job.objects.get(id=job_id)
            print("id", job.employer.user.id)
            if not job_applications.exists():
                return Response({'status': 'There is no application'}, status=status.HTTP_200_OK)
            elif job.employer.user.id == request.user.id:
                serializer = JobApplicationCandidateDetailsSerializer(job_applications, many=True)
                return Response({"data": serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({"message": "You are not allowed to show ."}, status=status.HTTP_400_BAD_REQUEST)
        except JobApplication.DoesNotExist:
            return Response({"message": "not found"}, status=status.HTTP_400_BAD_REQUEST)


class JobApplicationStatusUpdateAPIView(APIView):
    authentication_classes = [CustomAuthentication]
    permission_classes = [IsEmployer]
    def get(self, request, application_id):
        try:
            job_applications = JobApplication.objects.get(id=application_id)
            serializer = JobApplicationCandidateDetailsSerializer(job_applications)
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        except JobApplication.DoesNotExist:
            return Response({"message": "not found"}, status=status.HTTP_400_BAD_REQUEST)


    def patch(self, request, application_id):
        try:
            job_application = JobApplication.objects.get(id=application_id)
            if job_application.job.employer.user.id == request.user.id :
                job_application.status = request.data.get('status')
                job_application.save()
                return Response({"error": "Job Application's Status is updated."}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "You are not allowed to update this application."},
                                status=status.HTTP_400_BAD_REQUEST)
        except Job.DoesNotExist:
            return Response({"error": "No application found."}, status=status.HTTP_404_NOT_FOUND)



