from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
        extra_kwargs = {
            'mafvalue': {'required': False},
            'genovalue': {'required': False},
            'hewvalue': {'required': False},
            'infoscore': {'required': False}
        }

