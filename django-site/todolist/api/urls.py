# Dans api/urls.py
from django.urls import path
from django.views.generic import RedirectView
from .views import TaskListCreateView, TaskRetrieveUpdateDestroyView

urlpatterns = [
    path('', RedirectView.as_view(url='tasks/')),  # Redirige /api vers /api/tasks/
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDestroyView.as_view(), name='task-detail'),
]
