from django.shortcuts import render, redirect, render_to_response, HttpResponseRedirect
from django.http import HttpResponse, Http404
import datetime as dt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from .models import Project, Profile


# Create your views here.
def home(request):
    date = dt.date.today()
    projects = Project.get_projects()
    return render(request, 'index.html', {"date": date, "projects":projects})

def about(request):
    return render(request, 'about.html')

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
