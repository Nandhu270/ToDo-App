from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Todo
from django.contrib.auth.decorators import login_required

@login_required
def Home(request):
    user = request.user
    todo = Todo.objects.filter(user=user,is_completed=False)
    task_completed = Todo.objects.filter(user=user,is_completed=True)
    content = {
        'todo':todo,
        'done':task_completed,
    }
    return render(request,'index.html',content)

@login_required
def Add(request):
    task = request.POST['task']
    user = request.user
    Todo.objects.create(user=user, content=task)
    return redirect('index')

@login_required
def Done(request,id):
    user = request.user
    todo = Todo.objects.get(user=user,pk=id)
    todo.is_completed = True
    todo.save()
    return redirect('index')

@login_required
def Delete(request,id):
    return HttpResponse(id)

@login_required
def Edit(request,id):
    return HttpResponse(id)
    
@login_required
def Undone(request,id):
    user = request.user
    todo = Todo.objects.get(user=user,pk=id)
    todo.is_completed = False
    todo.save()
    return redirect('index')