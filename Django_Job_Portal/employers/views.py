from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import EmployerProfile
from .serializers import EmployerProfileSerializer
from accounts.authenticate import CustomAuthentication

class EmployerListView(APIView):
    authentication_classes = [CustomAuthentication]
    def put(self, request):
        """
        Update an existing Employer Profile (partial update).
        """
        try:
            user_profile = EmployerProfile.objects.get(user=request.user)
            serializer = EmployerProfileSerializer(user_profile, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except EmployerProfile.DoesNotExist:
            return Response({"error": "Employer profile not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": f"Failed to update employer profile: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request):
        """
        Get a specific Employer Profile by user ID or the current user's profile.
        """
        user_id = request.GET.get('user_id')
        try:
            if user_id:
                profile = EmployerProfile.objects.get(id=user_id)
            else:
                profile = EmployerProfile.objects.get(user=request.user)
            serializer = EmployerProfileSerializer(profile)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except EmployerProfile.DoesNotExist:
            return Response({"error": "Employer profile not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": f"An unexpected error occurred: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class EmployerDetailView(APIView):
    authentication_classes = [CustomAuthentication]
    def get(self, request):
        """
        Retrieve all Employer Profiles.
        """
        try:
            profiles = EmployerProfile.objects.all()
            serializer = EmployerProfileSerializer(profiles, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except EmployerProfile.DoesNotExist:
            return Response({"error": "No employer profiles found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": f"An unexpected error occurred: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
