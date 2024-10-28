from rest_framework import serializers

from applications.models import JobApplication
from candidates.models import CandidateProfile, CandidateSkills

class CandidateSkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CandidateSkills
        fields = '__all__'

class CandidateSerializer(serializers.ModelSerializer):
    skills = CandidateSkillsSerializer(read_only=True)
    class Meta:
        model = CandidateProfile
        fields = '__all__'

