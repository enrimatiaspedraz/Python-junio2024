from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Project, Task




def index(request):
    title = 'ACA VA UN VALOR'
    return render(request, 'index.html', {'title' : title})

def about(request):
    return render(request, 'about.html')

def projects(request):
    # projects = list(Project.object.values())
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects' : projects})
     
def tasks(request):
    # task = Task.objects.get(title=title)
    return render(request, 'task.html')