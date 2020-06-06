from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime
from pyuploadcare.dj.models import ImageField
from django_countries.fields import CountryField
from star_ratings.models import Rating
from django.db.models import ObjectDoesNotExist


# Create your models here.

class Profile(models.Model):
    profile_pic = models.ImageField()
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
