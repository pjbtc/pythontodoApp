# tasks/views.py
from django.shortcuts import render, redirect
from .models import Task

# View to display tasks
def task_list(request):
    tasks = Task.objects.all()  # Get all tasks
    return render(request, 'tasks/task_list.html', {'tasks': tasks})



