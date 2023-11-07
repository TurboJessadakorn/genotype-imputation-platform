from rest_framework import serializers
from .models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'  # Use '__all__' to include all fields of the model


class UserProfileEmailSerializer(serializers.ModelSerializer):
    # Define a SerializerMethodField to include the user's email
    user_email = serializers.SerializerMethodField()

    class Meta:
        model = UserProfile
        fields = ['user_id', 'role', 'organization', 'approval', 'user_email']

    # Custom method to fetch the user's email from the related User model
    def get_user_email(self, obj):
        return obj.user.email
