from rest_framework import serializers
from .models import *
from users.models import Profile

# Project
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('title','time_created', 'description', 'my_image', 'author', 'link', 'country')


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', 'profile_bio', 'profile_image',)