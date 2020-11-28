from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Task

def index(request):
    tasks = Task.objects.filter(completed=False)
    output = ', '.join([t.title for t in tasks])
    return HttpResponse(output)

def create(request):
    return render(request, 'todo/create.html', {})

def save(request):
    print(request.POST['title'])
    task = Task(title=request.POST['title'])
    task.save()
    return HttpResponseRedirect(reverse('todo:index'))