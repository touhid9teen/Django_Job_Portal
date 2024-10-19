from rest_framework import serializers

from candidates.models import CandidateProfile


class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CandidateProfile
        fields = '__all__'