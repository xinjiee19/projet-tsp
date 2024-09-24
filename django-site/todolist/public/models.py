from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)  # Category name

    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    due_date = models.DateField(null=True, blank=True)  # Deadline date, can be blank
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)  # Task can belong to a category

    def __str__(self):
        return self.title

