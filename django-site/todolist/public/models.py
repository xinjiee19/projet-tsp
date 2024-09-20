from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    due_date = models.DateField(null=True, blank=True)  # Champ date d'échéance, peut être vide

    def __str__(self):
        return self.title
