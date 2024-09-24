from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, Category
from .forms import TaskForm

# Display the list of tasks
def task_list(request):
    tasks = Task.objects.all()  # Fetch all tasks from the database
    categories = Category.objects.all()  # Fetch all categories
    return render(request, 'tasks/task_list.html', {'tasks': tasks, 'categories': categories})

# Create a new task
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')  # Redirect to the task list after creation
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})

# Update an existing task
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')  # Redirect to the task list after update
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form})

# Delete a task
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')  # Redirect after deletion
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})

# View to list all categories
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'categories/category_list.html', {'categories': categories})
