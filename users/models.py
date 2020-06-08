from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    profile_image = models.ImageField(upload_to='profile_pics')
    profile_bio = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    @classmethod
    def get_user_details(cls, current_user):
        user_details = Profile.objects.get(user=current_user)
        return user_details