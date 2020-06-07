from django.shortcuts import render, redirect, render_to_response, HttpResponseRedirect
from django.http import HttpResponse, Http404
import datetime as dt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from .models import Project, Profile
from .forms import NewProjectForm, ProfileUpdateForm

# Create your views here.
def home(request):
    date = dt.date.today()
    projects = Project.get_projects()
    return render(request, 'index.html', {"date": date, "projects":projects})

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

