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


# views.py
class CreateAndListApiview(APIView):
    authentication_classes = [CustomAuthentication]
    permission_classes = [IsCandidate]

    def post(self, request, job_id):
        cache_key = f"job_application_{request.user.id}_{job_id}"

        # Check if data exists in cache
        cached_data = cache.get(cache_key)
        if cached_data:
            return Response({'status': 'Already Applied'}, status=status.HTTP_200_OK)

        # Check in the database if the user already applied
        is_applied = JobApplication.objects.filter(candidate__user__id=request.user.id, job=job_id).exists()
        if is_applied:
            cache.set(cache_key, True)  # Cache this result for future requests
            return Response({'status': 'Already Applied'}, status=status.HTTP_200_OK)

        serializer = JobApplicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AllJobApplicationDetailsView(APIView):
    authentication_classes = [CustomAuthentication]
    permission_classes = [IsEmployer]

    def get(self, request, job_id):
        cache_key = f"job_applications_{job_id}"

        # Check cache first
        cached_applications = cache.get(cache_key)
        if cached_applications:
            return Response({"data": cached_applications}, status=status.HTTP_200_OK)

        job_applications = JobApplication.objects.filter(job_id=job_id)
        job = Job.objects.get(id=job_id)

        if not job_applications.exists():
            return Response({'status': 'There is no application'}, status=status.HTTP_200_OK)

        if job.employer.user.id == request.user.id:
            serializer = JobApplicationCandidateDetailsSerializer(job_applications, many=True)
            cache.set(cache_key, serializer.data)  # Cache the serialized data
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)

        return Response({"message": "You are not allowed to show."}, status=status.HTTP_400_BAD_REQUEST)


# views.py
class JobApplicationStatusUpdateAPIView(APIView):
    authentication_classes = [CustomAuthentication]
    permission_classes = [IsEmployer]

    def get(self, request, application_id):
        cache_key = f"job_application_status_{application_id}"

        # Check cache first
        cached_status = cache.get(cache_key)
        if cached_status:
            return Response({"data": cached_status}, status=status.HTTP_200_OK)

        try:
            job_application = JobApplication.objects.get(id=application_id)
            serializer = JobApplicationCandidateDetailsSerializer(job_application)
            cache.set(cache_key, serializer.data)  # Cache the serialized data
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        except JobApplication.DoesNotExist:
            return Response({"message": "not found"}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, application_id):
        try:
            job_application = JobApplication.objects.get(id=application_id)
            if job_application.job.employer.user.id == request.user.id:
                job_application.status = request.data.get('status')
                job_application.save()

                # Update cache after saving
                cache_key = f"job_application_status_{application_id}"
                cache.set(cache_key, {"status": job_application.status})

                return Response({"message": "Job Application's Status is updated."}, status=status.HTTP_200_OK)
            else:
                return Response({"message": "You are not allowed to update this application."},
                                status=status.HTTP_400_BAD_REQUEST)
        except JobApplication.DoesNotExist:
            return Response({"error": "No application found."}, status=status.HTTP_404_NOT_FOUND)




# class  CreateAndListApiview(APIView):
#     authentication_classes = [CustomAuthentication]
#     permission_classes = [IsCandidate]
#     def post(self, request, job_id):
#         # my_dinamic_cache_key = my_cache_key+str(job_id)
#
#         is_applied = JobApplication.objects.filter(candidate__user__id=request.user.id, job=job_id).exists()
#
#         if is_applied:
#             return Response({'status': 'Already Applied'}, status=status.HTTP_200_OK)
#         serializer = JobApplicationSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             print(serializer.data)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
#
# class AllJobApplicationDetailsView(APIView):
#     authentication_classes = [CustomAuthentication]
#     permission_classes = [IsEmployer]
#     def get(self, request, job_id):
#         try:
#             job_applications = JobApplication.objects.filter(job_id=job_id)
#             job = Job.objects.get(id=job_id)
#             print("id", job.employer.user.id)
#             if not job_applications.exists():
#                 return Response({'status': 'There is no application'}, status=status.HTTP_200_OK)
#             elif job.employer.user.id == request.user.id:
#                 serializer = JobApplicationCandidateDetailsSerializer(job_applications, many=True)
#                 return Response({"data": serializer.data}, status=status.HTTP_200_OK)
#             else:
#                 return Response({"message": "You are not allowed to show ."}, status=status.HTTP_400_BAD_REQUEST)
#         except JobApplication.DoesNotExist:
#             return Response({"message": "not found"}, status=status.HTTP_400_BAD_REQUEST)
#
#
# class JobApplicationStatusUpdateAPIView(APIView):
#     authentication_classes = [CustomAuthentication]
#     permission_classes = [IsEmployer]
#     def get(self, request, application_id):
#         try:
#             job_applications = JobApplication.objects.get(id=application_id)
#             serializer = JobApplicationCandidateDetailsSerializer(job_applications)
#             return Response({"data": serializer.data}, status=status.HTTP_200_OK)
#         except JobApplication.DoesNotExist:
#             return Response({"message": "not found"}, status=status.HTTP_400_BAD_REQUEST)
#
#
#     def patch(self, request, application_id):
#         try:
#             job_application = JobApplication.objects.get(id=application_id)
#             if job_application.job.employer.user.id == request.user.id :
#                 job_application.status = request.data.get('status')
#                 job_application.save()
#                 return Response({"error": "Job Application's Status is updated."}, status=status.HTTP_200_OK)
#             else:
#                 return Response({"error": "You are not allowed to update this application."},
#                                 status=status.HTTP_400_BAD_REQUEST)
#         except Job.DoesNotExist:
#             return Response({"error": "No application found."}, status=status.HTTP_404_NOT_FOUND)
#
#
#
