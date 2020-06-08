from rest_framework import serializers
from .models import *

# Project
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('title','time_created', 'description', 'my_image', 'author', 'link', 'country')
