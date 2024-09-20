from django.urls import path
from .views import TaskListCreateView, TaskRetrieveUpdateDestroyView

urlpatterns = [
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),  # URL pour lister ou créer des tâches
    path('tasks/<int:pk>/', TaskRetrieveUpdateDestroyView.as_view(), name='task-detail'),  # URL pour afficher, modifier ou supprimer une tâche
]
