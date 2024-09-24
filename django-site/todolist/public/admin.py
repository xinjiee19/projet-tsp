from django.contrib import admin
from .models import Task, Category  # Import Task and Category from public.models

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'due_date', 'completed', 'category')  # Display category as well
    list_filter = ('completed', 'due_date', 'category')  # Add category to filter options
    search_fields = ('title', 'description')  # Enable search for both title and description
    list_editable = ('completed',)  # Enable inline editing of the completed field
    ordering = ('-due_date',)  # Default ordering by due_date in descending order
    date_hierarchy = 'due_date'  # Add navigation by due_date at the top

# Admin class for Category
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Display category name
    search_fields = ('name',)  # Enable search by category name

# Register Task with TaskAdmin and Category with CategoryAdmin in the admin
admin.site.register(Task, TaskAdmin)
admin.site.register(Category, CategoryAdmin)
