from rest_framework.decorators import authentication_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from accounts.authenticate import CustomAuthentication
from accounts.permissions import IsCandidate, IsEmployer
from .models import JobApplication
from .serializers import JobApplicationSerializer


class JobApplicationView(APIView):
    authentication_classes = [CustomAuthentication]
    permission_classes = [IsCandidate]
    def post(self, request):
        is_applied = JobApplication.objects.filter(user=request.user.id).exists()
        if is_applied:
            return Response({'status': 'Already Applied'}, status=status.HTTP_200_OK)
        serializer = JobApplicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class JobApplicationListView(APIView):
    authentication_classes = [CustomAuthentication]
    permission_classes = [IsEmployer]
    def get(self, request):
        job_id = request.GET.get('job_id')
        user_id = request.GET.get('user_id')
        try:
            if job_id and user_id:
                jobApplications = JobApplication.objects.filter(job=job_id, candidate=user_id)
            else:
                jobApplications = JobApplication.objects.filter(job=job_id)
            serializer = JobApplicationSerializer(jobApplications, many=True)
            return Response(serializer.data)
        except JobApplication.DoesNotExist:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


