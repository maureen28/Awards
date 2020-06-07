from django import forms
from .models import Project
from django.contrib.auth.models import User


class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['author','profile', 'time_created']
        widgets = {
          'description': forms.Textarea(attrs={'rows':4, 'cols':10,}),
        }

