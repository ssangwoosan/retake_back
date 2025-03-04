from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list_list, name='todo_list_list'),
    path('<int:pk>/', views.todo_list_detail, name='todo_list_detail'),
    path('<int:pk>/delete/', views.todo_list_delete, name='todo_list_delete'),
    path('<int:pk>/edit/', views.todo_list_edit, name='todo_list_edit'),
    path('todos/<int:pk>/delete/', views.todo_delete, name='todo_delete'),
    path('todos/<int:pk>/edit/', views.todo_edit, name='todo_edit'),
]