from django.db import models
from django.contrib.auth.models import User
from pyuploadcare.dj.models import ImageField
from django_countries.fields import CountryField

# Create your models here.

class Profile(models.Model):
    profile_pic = models.ImageField()
    bio = models.CharField(max_length=100)
    user = models.ForeignKey(User,blank=True, on_delete=models.CASCADE, related_name="profile")

    def __str__(self):
        return self.bio

    #Save profile
    def profile_save(self):
        self.save()

     #delete profile
    def delete_profile(self):
        self.delete()