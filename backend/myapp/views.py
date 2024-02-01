from django.shortcuts import get_object_or_404
from .models import Movie, Review, MovieCollection, Event, MovieCollection, DiscussionBoard, Comment, User, RSVP, Like
from .serializers import (ReviewSerializer, MovieCollectionSerializer, MovieSerializer, MovieCollectionSerializer, DiscussionBoardSerializer CommentSerializer, EventSerializer, RSVPSerializer )
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
import requests
from django.conf import settings
from django.http import JsonResponse, HttpResponse

def home(request): 
    return HttpResponse("Welcome to my Django App")

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

class MovieCollectionViewSet(viewsets.ModelViewSet):
    queryset = MovieCollection.objects.all()
    serializer_class = MovieCollectionSerializer
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsAuthenticatedOrReadOnly]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class DiscussionBaordViewSet(viewsets.ModelViewSet):
    queryset = DiscussionBoard.objects.all()
    serializer_class = DiscussionBoardSerializer
    persmission_classes = [IsAuthenticatedOrReadOnly]
    
class CommentViewSet(viewsets.ModelViewSet):
    queryset = CommentBoard.objects.all()
    serializer_class = CommentSerializer 
    permission_classes = [IsAuthenticatedOrReadOnly]
    
