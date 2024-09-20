from django.contrib import admin
from .models import Task  # Importer Task depuis public.models

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'completed')  # Colonnes affichées dans l'admin
    list_filter = ('completed',)  # Filtres sur la droite
    search_fields = ('title',)  # Barre de recherche

# Enregistrer le modèle Task avec la classe TaskAdmin dans l'admin
admin.site.register(Task, TaskAdmin)
