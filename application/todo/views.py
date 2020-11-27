from django.shortcuts import render
from django.http import HttpResponse
from .models import Task

def index(request):
    tasks = Task.objects.filter(completed=False)
    output = ', '.join([t.title for t in tasks])
    return HttpResponse(output)