from django.shortcuts import get_object_or_404
from .models import Project, Movie, Review, Comment, Like, Event, DiscussionBoard, RSVP 
from .serializers import ProjectSerializer, ReviewSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
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
    
    def perform_create(self, serializer):
        movie_id = self.kwargs.get('movie_id', None)
        movie = get_object_or_404(Movie, pk=movie_id)
        serializer.save(user=self.request.user, movie=movie)
