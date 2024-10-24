from rest_framework import serializers

from candidates.models import CandidateProfile, CandidateSkills


class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CandidateProfile
        fields = '__all__'

class CandidateSkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CandidateSkills
        fields = '__all__'