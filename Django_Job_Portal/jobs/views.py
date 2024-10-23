from django.http import JsonResponse
from rest_framework.decorators import permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Job
from .serializers import JobSerializer
from accounts.authenticate import CustomAuthentication
from accounts.permissions import IsEmployer
from django_filters.rest_framework import DjangoFilterBackend
from .filters import JobFilter


class JobListView(APIView):
    authentication_classes = [CustomAuthentication]
    def get(self, request):
        try:
            total_jobs = Job.objects.filter(is_deleted=False).count()
            jobs = Job.objects.filter(is_deleted=False)
            serializer = JobSerializer(jobs, many=True)
            return Response({"Total Job" : total_jobs,"jobs":serializer.data}, status=status.HTTP_200_OK)
        except Job.DoesNotExist:
            return Response({"error": "No jobs found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": f"An unexpected error occurred: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request):
        job = Job.objects.get(id=request.GET.get('job_id'))
        serializer = JobSerializer(job, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        try:
            # todo: update this query and only job created_user only delete this job------------------------------
            print("user", request.user.id)
            job = Job.objects.get(id=request.GET.get('job_id'), employer=request.user.id)
            if job.is_deleted == True:
                return Response({"error": "Job is already deleted."}, status=status.HTTP_400_BAD_REQUEST)
            job.is_deleted = True
            job.save()
            return Response({"error": "Job is deleted."},status=status.HTTP_200_OK)
        except Job.DoesNotExist:
            return Response({"error": "No jobs found."}, status=status.HTTP_404_NOT_FOUND)

class JobPostView(APIView):
    authentication_classes = [CustomAuthentication]
    permission_classes = [IsEmployer]

    def post(self, request):
        serializer = JobSerializer(data=request.data)

        if serializer.is_valid():
            try:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({"error": f"Failed to create job: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class JobFilterView(APIView):
    authentication_classes = [CustomAuthentication]
    filter_backends = [DjangoFilterBackend]
    filterset_class = JobFilter
    def get(self, request, *arg, **kwargs):
        try:
            jobs = Job.objects.filter(is_deleted=False)
            filter_backends = DjangoFilterBackend()
            filter_queryset = filter_backends.filter_queryset(request, jobs, self)
            total_jobs = filter_queryset.count()
            serializer = JobSerializer(filter_queryset, many=True)
            return Response({"Total Job" : total_jobs,"jobs":serializer.data}, status=status.HTTP_200_OK)
        except Job.DoesNotExist:
            return Response({"error": "No jobs found."}, status=status.HTTP_404_NOT_FOUND)

