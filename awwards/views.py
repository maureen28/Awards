from django.shortcuts import render, redirect, render_to_response, HttpResponseRedirect
from django.http import HttpResponse, Http404
import datetime as dt
from django.conf import settings
from django.templatetags.static import static
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from .models import Project, Profile
from .forms import NewProjectForm, ProfileUpdateForm, RegistrationForm
from django.contrib import messages
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer, ProjectSerializer


# Create your views here.
def home(request):
    date = dt.date.today()
    projects = Project.get_projects()
    return render(request, 'index.html', {"date": date, "projects":projects})

# Registration
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('/login')
    else:
        form = RegisterForm()
    return render(request, 'registration/registration_form.html', {'form':form})

def about(request):
    return render(request, 'about.html')

# New project
@login_required(login_url='/accounts/login/')
def new_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.author = current_user
            project.save()
        return redirect('home')

    else:
        form = NewProjectForm()
    return render(request, 'projects/new-project.html', {"form": form})

def get_project(request, id):

    try:
        project = Projects.objects.get(pk = id)

    except ObjectDoesNotExist:
        raise Http404()
    return render(request, "projects/projects.html", {"project":project})


# search
@login_required(login_url='/accounts/login/')
def search_results(request):
    if 'keyword' in request.GET and request.GET["keyword"]:
        search_term = request.GET.get("keyword")
        searched_projects = Project.search_projects(search_term)
        message = f"{search_term}"
        return render(request, 'search.html', {"message":message,"projects": searched_projects})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message": message})

@login_required(login_url='/accounts/login/')
def profile_display(request):
    current_user = request.user
    author = current_user
    projects = Project.get_by_author(author)
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile(user=request.user)
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
        return redirect('profile')
    else:
        form = ProfileUpdateForm()
    return render(request, 'registration/profile.html', {"form":form, "projects":projects})


# class ProjectList(APIView):
#     def get(self, request, format=None):
#         all_project = Projects.objects.all()
#         serializers = ProjectSerializer(all_project, many=True)
#         return Response(serializers.data)

# class ProfileList(APIView):
#     def get(self, request, format=None):
#         all_profile = Profile.objects.all()
#         serializers = ProfileSerializer(all_profile, many=True)
#         return Response(serializers.data)