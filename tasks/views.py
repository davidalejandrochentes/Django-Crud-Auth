from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib import messages
from .forms import TaskForm
from .models import Task
from django.utils import timezone
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request, 'tasks/home.html', {})

@login_required
def tasks(request):
    tasks = Task.objects.filter(user=request.user, datecompleted__isnull=True,title__contains=request.GET.get('search', '')).order_by('-created')
    context = {
        'quantity': len(tasks),
        'pagina': "pendientes",
        'tasks': tasks,
    }
    return render(request, 'tasks/tasks.html', context)

@login_required
def tasks_completed(request):
    tasks = Task.objects.filter(user=request.user, datecompleted__isnull=False).order_by('-created')
    quantity = len(tasks)
    context = {
        'quantity': len(tasks),
        'pagina': "completadas",
        'tasks': tasks,
    }
    return render(request, 'tasks/tasks.html', context)

@login_required
def create_tasks(request):
    if request.method == 'GET':
        return render(request, 'tasks/create_task.html', {'form': TaskForm})
    else:
        try:
            form = TaskForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('tasks')
        except ValueError:
            messages.success(request, "por favor ingrese datos validos")
            return render(request, 'tasks/create_task.html', {'form': TaskForm})

@login_required
def view_tasks(request, id):
    task = get_object_or_404(Task, id = id, user=request.user)
    context = {
      'task': task
    }
    return render(request, 'tasks/detail.html', context)

@login_required
def completed_tasks(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)
    if request.method == 'POST':
        task.datecompleted = timezone.now()
        task.save()
        return redirect('tasks')

@login_required
def delete_tasks(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)
    task.delete()
    return redirect ('tasks')        

@login_required
def edit_tasks(request, id):
    if request.method == 'GET':
        task = get_object_or_404(Task, id = id, user=request.user)   
        form = TaskForm(instance= task)
        context = {
            'form': form,
            'id': id,
        }
        return render(request, 'tasks/edit_task.html', context)
    
    if request.method == 'POST':
        try:
            task = get_object_or_404(Task, id = id, user=request.user)
            form = TaskForm(request.POST, instance= task)
            if form.is_valid():
                form.save()
            context = {'form': form,'id': id,}  
            messages.success(request, "Update Task")  
            return render(request, 'tasks/edit_task.html', context)
        except ValueError:
            context = {'form': form,'id': id,}  
            messages.success(request, "Error")  
            return render(request, 'tasks/edit_task.html', context)

@login_required
def log_out(request):
    logout(request)
    return redirect('home')

def sign_up(request):
    if request.method == 'GET':
        return render(request, 'tasks/singup.html', {'form': UserCreationForm})
    
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('tasks')
            except IntegrityError:
                messages.success(request, "El usuario ya existe")
                return render(request, 'tasks/singup.html', {'form': UserCreationForm})

        messages.success(request, "Las contraseñas no coinciden")
        return render(request, 'tasks/singup.html', {'form': UserCreationForm})

def log_in(request):
    if request.method =='GET':
        return render(request, 'tasks/login.html', {'form': AuthenticationForm})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            messages.success(request, "El usuario no existe, o la password es incorrecta")
            return render(request, 'tasks/login.html', {'form': AuthenticationForm})
        else:
            login(request, user)
            return redirect('tasks')