from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Task

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == "POST":
        title = request.POST.get('title', '')
        description = request.POST.get('description', '')
        due_date = request.POST.get('due_date', '')
        if title:
            Task.objects.create(title=title, description=description)
        return redirect('task_list')
    return render(request, 'add_task.html')

def delete_task(request, task_id):
    Task.objects.get(id=task_id).delete()
    return HttpResponseRedirect(reverse('task_list'))

def toggle_completed(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = not task.completed
    task.save()
    return HttpResponseRedirect(reverse('task_list'))