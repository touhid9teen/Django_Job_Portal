from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from accounts.authenticate import CustomAuthentication
from accounts.permissions import IsCandidate, IsEmployer
from jobs.models import Job
from .models import JobApplication
from .serializers import (
    JobApplicationSerializer,
    JobApplicationCandidateDetailsSerializer
)


class CreateAndListApiview(APIView):
    authentication_classes = [CustomAuthentication]
    permission_classes = [IsCandidate]
    def post(self, request, job_id):
        is_applied = JobApplication.objects.filter(candidate__user__id=request.user.id, job=job_id).exists()
        if is_applied:
            return Response({'status': 'Already Applied'}, status=status.HTTP_200_OK)
        serializer = JobApplicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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



