from django.shortcuts import render
from django.http import JsonResponse
from .models import Article

def article_all(request):
    articles = Article.objects.all()
    data = [{"id": article.id, "title": article.title} for article in articles]
    return JsonResponse(data, safe=False)

def article_id(request, id):
    try:
        article = Article.objects.get(id=id)
        data = {"id": article.id, "title": article.title}
        return JsonResponse(data)
    except Article.DoesNotExist:
        return JsonResponse({"error": "Article not found"})