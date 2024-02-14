from django.shortcuts import get_object_or_404
from .models import Movie, Review, MovieCollection, Event, DiscussionBoard, Comment, RSVP, Like
from .serializers import (ReviewSerializer, MovieCollectionSerializer, MovieSerializer, 
                          DiscussionBoardSerializer, CommentSerializer, EventSerializer, 
                          RSVPSerializer)
from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework import generics, viewsets, status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
import requests
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import action 
from rest_framework import filters 
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from .serializers import UserRegistrationSerializer

# main_app/views.py

from rest_framework import generics, status, permissions
from rest_framework.response import Response # modify these imports to match
...
# include the following imports
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
...
from .serializers import UserSerializer # add the UserSerizlier to the list
...
from django.http import JsonResponse 
from .api_client import ThirdPartyAPIClient

def get_resource(request, resource_id):
    try: 
        data = ThirdPartyAPIClient.get_resource(resource_id)
        return JsonResponse(data)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

# include the registration, login, and verification views below
# User Registration
class CreateUserView(generics.CreateAPIView):
  permission_classes = [AllowAny]
  queryset = User.objects.all()
  serializer_class = UserSerializer

  def create(self, request, *args, **kwargs):
    response = super().create(request, *args, **kwargs)
    user = User.objects.get(username=response.data['username'])
    refresh = RefreshToken.for_user(user)
    return Response({
      'refresh': str(refresh),
      'access': str(refresh.access_token),
      'user': response.data
    })

class UserRegistrationAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_BAD_REQUEST)
# User Login
class LoginView(APIView):
  permission_classes = [AllowAny]

  def post(self, request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user:
      refresh = RefreshToken.for_user(user)
      return Response({
        'refresh': str(refresh),
        'access': str(refresh.access_token),
        'user': UserSerializer(user).data
      })
    return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)

# User Verification
class VerifyUserView(APIView):
  permission_classes = [permissions.IsAuthenticated]

  def get(self, request):
    user = User.objects.get(username=request.user)  # Fetch user profile
    refresh = RefreshToken.for_user(request.user)  # Generate new refresh token
    return Response({
      'refresh': str(refresh),
      'access': str(refresh.access_token),
      'user': UserSerializer(user).data
    })



def home(request): 
    return HttpResponse("Welcome to my Django App")

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['genre', 'director']
    search_fields = ['title', 'plot']

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

class DiscussionBoardViewSet(viewsets.ModelViewSet):
    queryset = DiscussionBoard.objects.all()
    serializer_class = DiscussionBoardSerializer
    persmission_classes = [IsAuthenticatedOrReadOnly]
    
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer 
    permission_classes = [IsAuthenticatedOrReadOnly]
    
class LikeCreateDestroyView(generics.CreateAPIView, generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        like, created = Like.objects.get_or_create(user=request.user, comment=comment)
        if created: 
            return Response(status=status.HTTP_201_CREATED)
        else: 
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        try: 
            like = Like.objects.get(user=request.user, comment=comment)
            like.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Like.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
class RSVPViewSet(viewsets.ModelViewSet):
    queryset = RSVP.objects.all()
    serializer_class = RSVPSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def rsvp(self, request, pk=None):
        pass 
        # Implementation for RSVPing to an event

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def mark_completed(self, request, pk=None):
        pass
        # Implementation for marking an event as completed

    


# In your view
class UserRegistrationAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
