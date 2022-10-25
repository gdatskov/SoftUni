from django.shortcuts import render
from django import http

from djangoProject101.tasks.models import Task


def show_bare_minimum_view(request):
    return http.HttpResponse('not 404')


def get_all_tasks(request):
    all_tasks = Task.objects.order_by('id').all()
    result = ", ".join(f'{t.name}({t.id})' for t in all_tasks)
    # print(list(all_tasks))
    return http.HttpResponse(result)


def index1(request):
    return render(request, 'index.html')


def index2(request):
    all_tasks = Task.objects.order_by('id').all()
    context = {
        'title': 'Tasks app',
        'tasks': all_tasks
    }
    return render(request, 'index2.html', context)
