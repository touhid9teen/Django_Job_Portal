from rest_framework.decorators import authentication_classes
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

class UpdateAndDeleteApiView(APIView):
    authentication_classes = [CustomAuthentication]
    permission_classes = [IsEmployer]
    def get(self, request):
        job_id = request.GET.get('job_id')
        user_id = request.GET.get('user_id')
        try:
            if job_id and user_id:
                jobApplications = JobApplication.objects.filter(job=job_id, candidate=user_id)
                total_job = jobApplications.count()
            else:
                jobApplications = JobApplication.objects.filter(job=job_id)
                total_job = jobApplications.count()
            serializer = JobApplicationCandidateDetailsSerializer(jobApplications, many=True)
            return Response({'Tolal_Applied': total_job, "Applied_Job": serializer.data}, status=status.HTTP_200_OK)
        except JobApplication.DoesNotExist:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        job_id = request.GET.get('job_id')
        user_id = request.GET.get('user_id')
        try:
            job = Job.objects.get(id=job_id)
            job_application = JobApplication.objects.get(job=job_id, candidate=user_id)
            print('job_application', job_application.id)
            if job.is_deleted:
                return Response({"error": "Job is already deleted."}, status=status.HTTP_400_BAD_REQUEST)

            if job.employer.user.id == request.user.id :
                job_application.status = request.data.get('status')
                job_application.save()
                return Response({"error": "Job Application's Status is updated."}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "You are not allowed to update this application."},
                                status=status.HTTP_400_BAD_REQUEST)
        except Job.DoesNotExist:
            return Response({"error": "No application found."}, status=status.HTTP_404_NOT_FOUND)



