from django.urls import path
from .import views

urlpatterns = [
    path('articles/', views.article_all),
    path('articles/<int:id/>/', views.article_id),
]
