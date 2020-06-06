from rest_framework import serializers
from .models import Project,Profile

# Profile
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', 'bio', 'profile_pic')

# Project
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('title','time_created', 'description', 'my_image', 'author', 'link', 'country', 'profile')
