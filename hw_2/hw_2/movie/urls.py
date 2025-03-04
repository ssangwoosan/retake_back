from django.urls import path
from .import views

urlpatterns = [
    path('movies/', views.movie_all),
    path('movies/<int:id/>/', views.movie_id),
]