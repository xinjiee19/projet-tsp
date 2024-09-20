from rest_framework import serializers
from public.models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'completed', 'due_date']  # Ajout de due_date
