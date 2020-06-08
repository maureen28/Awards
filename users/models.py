from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    profile_image = models.ImageField(upload_to='profile_pics')
    profile_bio = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')