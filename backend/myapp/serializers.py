from rest_framework import serializers
from .models import Movie, Review, Event, DiscussionBoard, Comment, User, RSVP 


class ProjectSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Movie 
        fields ='__all__'
        
class UserSerializer(serializers.UserSerializer):
    class Meta: 
        model = User
        fields = ['id', 'username', 'profile_image']
        
class ReviewSerializer(serializers.ReviewSerializer):
    user = UserSerializer(read_only=True) 
    
    class Meta: 
        model = Review 
        fields = ['id', 'user', 'text', 'rating', 'created_at', 'updated_at']

class MovieSerializer(serializers.MovieSerializer):
        reviews = ReviewSerializer(many=True, read_only=True)
        
        class Meta: 
            model = Movie
            fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Comment
        fields = ['id', 'text', 'user', 'created_at']
        
class EventSerializer(serializers.ModelSerializer):
    attendees = UserSerializer(many=True, read_only = True)
    invitees = UserSerializer(many=True, read_only = True)
    
    class Meta: 
        model = Event
        fields = ['id', 'title', 'date', 'location']
        
class DiscussionBoardSerializer(serializers.DiscussionBoardSerializer):
    comments = CommentSerializer(many=True, read_only = True)
    
    class Meta: 
        model = DiscussionBoard
        fields = '__all__'
        
class RSVPSerializer(serializers.RSVPSerializer):
    event = EventSerializer(read_only=True)
    
    class Meta: 
        model = RSVP 
        fields = '__all__'
        
