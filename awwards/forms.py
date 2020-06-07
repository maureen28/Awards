from django import forms
from .models import Profile, Project
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from registration.forms import RegistrationForm
from crispy_forms.helper import FormHelper


class RegisterForm(RegistrationForm):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    class Meta:
        model = User
        fields = ('username', 'name', 'email', 'password1', 'password2',)

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
        self.helper.form_show_labels = True

class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['author','profile', 'time_created']
        widgets = {
          'description': forms.Textarea(attrs={'rows':4, 'cols':10,}),
        }

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']