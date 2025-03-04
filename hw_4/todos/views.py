from django.shortcuts import render
from .models import TodoList, Todo
from .forms import TodoListForm, TodoForm
# Create your views here.

def todo_list_list(request):
    todo_lists = TodoList