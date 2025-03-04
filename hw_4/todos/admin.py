from django.contrib import admin
from .models import TodoList, Todo
# Register your models here.

@admin.register(TodoList)
class TodoListAdmin(TodoList):
    list_display = ('title', 'description')

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'due_date', 'status', 'todo_list')