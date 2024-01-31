from django.shortcuts import render
from .models import Project, Movie, Review, Comment, Like, Event, DiscussionBoard, RSVP 
from .serializers import ProjectSerializer
from rest_framework import generics
import requests
from django.conf import settings
from django.http import JsonResponse
from django.http import HttpResponse

def home(request): 
    return HttpResponse("Welcome to my Django App")

class ProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

def search_movie(request, title):
    api_key = settings.OMDB_API_KEY
    url = f"http://www.omdbapi.com/?apikey={api_key}&t={title}"
    response = requests.get(url)
    movie_data = response.json()
    return JsonResponse(movie_data)

class CreateReviewView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
