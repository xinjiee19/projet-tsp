from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed', 'due_date']  # Ajout de due_date
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'})  # Affiche un sélecteur de date HTML5
        }
