from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

# Affiche la liste des tâches
def task_list(request):
    tasks = Task.objects.all()  # Récupère toutes les tâches de la base de données
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

# Crée une nouvelle tâche
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')  # Redirige vers la liste des tâches après création
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})

# Modifie une tâche existante
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')  # Redirige vers la liste des tâches après modification
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form})

# Supprime une tâche
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')  # Redirige après la suppression
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})
