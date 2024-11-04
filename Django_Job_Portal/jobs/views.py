from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets

from employers.models import EmployerProfile
from .models import Job
from .serializers import JobSerializer, JobDetailSerializer, JobCreateSerializer
from accounts.authenticate import CustomAuthentication
from accounts.permissions import IsEmployer
from django_filters.rest_framework import DjangoFilterBackend
from .filters import JobFilter


class CreateAndListApiview(APIView):
    authentication_classes = [CustomAuthentication]
    permission_classes = [IsEmployer]

    def post(self, request):
        serializer = JobCreateSerializer(data=request.data)
        if serializer.is_valid():
            try:
                validated_data = serializer.validated_data
                Job.objects.create_job(**validated_data)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({"error": f"Failed to create job: {str(e)}"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        try:
            jobs = Job.objects.filter(is_deleted=False, employer__user__id=request.user.id)
            serializer = JobSerializer(jobs, many=True)
            total_jobs = jobs.count()
            return Response({"Total Job" : total_jobs,"jobs":serializer.data}, status=status.HTTP_200_OK)
        except Job.DoesNotExist:
            return Response({"error": "No jobs found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": f"An unexpected error occurred: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class UpdateAndDeleteApiView(APIView):
    authentication_classes = [CustomAuthentication]
    def get(self, request, job_id):
        try:
            job = Job.objects.get(id=job_id)
            serializer = JobDetailSerializer(job)
            return Response(serializer.data)
        except Job.DoesNotExist:
            return Response({"error": "No job found."}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, job_id):
        job = Job.objects.get(id=job_id)
        serializer = JobSerializer(job, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, job_id):
        try:
            job = Job.objects.get(id=job_id, employer__user__id=request.user.id)
            if job.is_deleted:
                return Response({"error": "Job is already deleted."}, status=status.HTTP_400_BAD_REQUEST)

            if job.employer.user.id == request.user.id:
                job.is_deleted = True
                job.save()
                return Response({"error": "Job is deleted."},status=status.HTTP_200_OK)
            else:
                return Response({"error": "You are not allowed to delete this job."},status=status.HTTP_400_BAD_REQUEST)
        except Job.DoesNotExist:
            return Response({"error": "No jobs found."}, status=status.HTTP_404_NOT_FOUND)


class JobFilterView(APIView):
    authentication_classes = [CustomAuthentication]
    filter_backends = [DjangoFilterBackend]
    filterset_class = JobFilter
    def get(self, request, *arg, **kwargs):
        try:
            jobs = Job.objects.filter(is_deleted=False)

            #Appley filtering
            filter_backends = DjangoFilterBackend()
            filter_queryset = filter_backends.filter_queryset(request, jobs, self)
            total_jobs = filter_queryset.count()

            #Apply Pageination
            pageinator = PageNumberPagination()
            pageinator.page_size = 10
            pageinatorquery = pageinator.paginate_queryset(filter_queryset, request)

            # total_jobs = filter_queryset.count()
            serializer = JobDetailSerializer(pageinatorquery, many=True)
            return Response({
                "total_jobs": total_jobs,
                "data":serializer.data}, status=status.HTTP_200_OK)
        except Job.DoesNotExist:
            return Response({"error": "No jobs found."}, status=status.HTTP_404_NOT_FOUND)
