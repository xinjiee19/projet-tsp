from django.shortcuts import render
from rest_framework import generics
from public.models import Task
from .serializers import TaskSerializer

# Lister toutes les tâches ou créer une nouvelle tâche
class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# Détail, mise à jour, et suppression d'une tâche
class TaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
