from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from accounts.permissions import IsAdmin
from .models import SubscriptionPlan
from .serializers import SubscriptionSerializer, SubscriptionPlanSerializer
from accounts.authenticate import CustomAuthentication



class MakeSubscriptionView(APIView):
    authentication_classes = [CustomAuthentication]
    permission_classes = [IsAdmin]
    def post(self, request):
        serializer = SubscriptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        try:
            subscriptions = SubscriptionPlan.objects.all()
            serializer = SubscriptionSerializer(subscriptions, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

# todo: update and delete api
class ChosenSubscriptionView(APIView):
    authentication_classes = [CustomAuthentication]

    def post(self, request):
        serializer = SubscriptionPlanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# todo: index db
