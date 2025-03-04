from django.shortcuts import render
from django.http import JsonResponse
from .models import Movie
# Create your views here.

def movie_all(request):
    movies = Movie.objects.all()
    data = [{"id" : movie.id, "title": movie.title} for movie in movies]
    return JsonResponse (data, safe=False)

def movie_id(request, id):
    try:
        movies = Movie.objects.get(id=id)
        data = [{"id" : movie.id, "title": movie.title} for movie in movies]
        return JsonResponse (data)
    except:
        return JsonResponse({"error": "Movie not Found"})
