from django.shortcuts import render, redirect, render_to_response, HttpResponseRedirect
from django.http import HttpResponse, Http404
import datetime as dt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from friendship.exceptions import AlreadyExistsError

from .models import Project, Profile


# Create your views here.
def home(request):
    date = dt.date.today()
    projects = Project.get_projects()

    return render(request, 'index.html', {"date": date, "projects":projects})
