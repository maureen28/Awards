from django.shortcuts import render, redirect, render_to_response, HttpResponseRedirect
from django.http import HttpResponse, Http404
import datetime as dt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from .models import Project
from .forms import NewProjectForm
from django.contrib import messages
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import *
from django.contrib.auth.views import LogoutView
from rest_framework import status
from .permissions import IsAdminOrReadOnly

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


@login_required(login_url='/accounts/login')
def project(request, project_id):
    try:
        project = Project.objects.get(id=project_id)
    except Project.DoesNotExist:
        raise Http404()
    return render(request, "projects/projects.html", locals())


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


class ProjectList(APIView):
    def get(self, request, format=None):
        all_project = Project.objects.all()
        serializers = ProjectSerializer(all_project, many=True)
        return Response(serializers.data)
    
# class ProfileList(APIView):
#     def get(self, request, format=None):
#         all_profile = Profile.objects.all()
#         serializers = ProfileSerializer(all_profile, many=True)
#         return Response(serializers.data)