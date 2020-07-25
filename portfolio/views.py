from django.shortcuts import render
from django.http import HttpRequest
from .models import Project, Award
# Create your views here.


def home(request):
    return render(request, "portfolio/home.html")


def project(request):
    global projects
    projects = Project.objects.all()
    context = {
        'projects': projects,
    }
    return render(request, 'portfolio/projects.html', context)


def award(request):
    global projects
    awards = Award.objects.all()
    context = {
        'awards': awards,
    }
    return render(request, 'portfolio/award.html', context)
