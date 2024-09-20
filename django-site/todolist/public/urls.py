from django.urls import path
from .views import task_list, task_create, task_update, task_delete
from . import views


urlpatterns = [
    path('tasks/', task_list, name='task_list'),
    path('', views.task_list, name='task-list'),
    path('', task_list, name='task_list'),  # URL pour afficher la liste des tâches
    path('create/', task_create, name='task_create'),  # URL pour créer une nouvelle tâche
    path('update/<int:pk>/', task_update, name='task_update'),  # URL pour modifier une tâche
    path('delete/<int:pk>/', task_delete, name='task_delete'),  # URL pour supprimer une tâche

]
