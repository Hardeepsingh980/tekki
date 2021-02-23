from rest_framework import serializers
from .models import UserSubscription

class UserSubscriptionSerialiser(serializers.ModelSerializer):

    class Meta:
        model = UserSubscription
        fields = '__all__'