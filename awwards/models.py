from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime
from pyuploadcare.dj.models import ImageField
from django_countries.fields import CountryField
from django.db.models import ObjectDoesNotExist
from django.http import Http404

# Create your models here.

class Profile(models.Model):
    profile_pic = ImageField()
    bio = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.bio

    #Save profile
    def profile_save(self):
        self.save()

     #delete profile
    def delete_profile(self):
        self.delete()

# Project model

class Project(models.Model):
    title = models.CharField(max_length=120)
    time_created = models.DateTimeField(default=datetime.now)
    description = models.TextField()
    my_image = ImageField()
    link = models.URLField()
    country = CountryField(blank_label='(select country)', default='Kenya')
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    profile = models.ForeignKey(Profile)

    def __str__(self):
        return self.title

    #Save project
    def save_project(self):
        self.save()

    #Delete project
    def delete_project(self):
        self.delete()

    #Get project
    @classmethod
    def get_projects(cls):
        projects = cls.objects.all()
        return projects

    # If doesnt exist
    @classmethod
    def get_project(request, id):
        try:
            project = Projects.objects.get(pk = id)

        except ObjectDoesNotExist:
            raise Http404()

        return project

    #Search project
    @classmethod
    def search_projects(cls, search_term):
        projects = cls.objects.filter(project_title__icontains=search_term)
        return projects


    @classmethod
    def get_by_author(cls, author):
        projects = cls.objects.filter(author=author)
        return projects

