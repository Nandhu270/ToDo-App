from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Todo
from django.contrib.auth.decorators import login_required

@login_required
def Home(request):
    logged = request.user
    todo = logged.todo.all()
    content = {
        'todo':todo
    }
    return render(request,'index.html',content)

@login_required
def Add(request):
    task = request.POST['task']
    logged = request.user
    Todo.objects.create(user=logged, content=task)
    return redirect('index')
    
