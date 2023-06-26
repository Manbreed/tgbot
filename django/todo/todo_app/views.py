from datetime import datetime

from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

from django.http import HttpResponse

from todo_app.models import TodoTask, TodoStatus, TodoList


def index(request: WSGIRequest):
    if request.method == 'POST':
        action_type = request.POST.get('type')
        if action_type == 'create':
            __create_task(request)
        if action_type == 'destroy':
            TodoTask.objects.get(pk=request.POST.get('task_id')).delete()
        """    
            task_id = request.POST.get('task_id')
            todo = TodoTask.objects.get(pk=task_id)
            todo.delete()
           """
    all_tasks = TodoTask.objects.all().order_by('-id')

        # можно сократить посмотреть в лекции
        # TodoTask.objects.get(pk=request.POST.get('task_id')).delete()
    # print(request.POST.get('name'))
    return render(request, 'index.html', {
        #'tasks_array': TodoTask.objects.all().order_by('-id'),
            'tasks_array' : all_tasks
    })


def __create_task(request):
    todo = TodoTask()
    todo.title = request.POST.get('title')
    todo.status = TodoStatus.objects.get(pk=TodoStatus.C_NOT_COMPLETED)
    todo.create_at = datetime.now()
    todo.text = ''
    todo.todo_list = TodoList.objects.get(pk=1)
    todo.save()
