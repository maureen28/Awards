from django import forms
from .models import Profile, Project
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper


class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = [ 'time_created', 'user']
        widgets = {
          'description': forms.Textarea(attrs={'rows':4, 'cols':10,}),
        }

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']