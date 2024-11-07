from rest_framework import serializers
from .models import SubscriptionPlan, UserSubscription


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionPlan
        fields = '__all__'

class SubscriptionPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSubscription
        fields = '__all__'

    # def validate(self, data):
    #     print("data", data)
    #     if data.user.user_type == 'employer' and data.plan.name != 'enterprise':
    #         raise serializers.ValidationError("Employer only can chose Enterprise plan")
    #     if data.user.user_type == 'candidate' and data.plan.name == 'enterprise':
    #         raise serializers.ValidationError("Candidate can not chose Enterprise plan")



    # def __init__(self):
    #     self.error = None
    #     self.data = None
    #
    # def is_valid(self):
    #     pass
    #
    # def save(self):
    #     pass
