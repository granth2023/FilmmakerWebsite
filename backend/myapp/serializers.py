from rest_framework import serializers
from .models import Movie, Review, Event, DiscussionBoard, Comment, RSVP, MovieCollection, User
# from django.conf import settings
from django.contrib.auth.models import User 

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta: 
        model = User 
        fields = ('id', 'username', 'email', 'password')
        
    def create(self, validated_data): 
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        
        return user 
    





class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    
    class Meta:
        model = Review
        fields = ['id', 'user', 'text', 'rating', 'created_at']

# Corrected base class and included reviews properly
class MovieSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)  # Ensure your Movie model has a reverse relation to Review that allows 
    average_rating = serializers.SerializerMethodField() 
    
    def get_average_rating(self, movie):
        reviews = movie.reviews.all()
        if reviews.exists(): 
            return sum([review.rating for review in reviews]) / reviews.count()
        return 0

    
    class Meta:
        model = Movie
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'  # Adjusted to include all fields for simplicity

class EventSerializer(serializers.ModelSerializer):
    attendees = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    invitees = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    attendee_count = serializers.SerializerMethodField()

    def get_attendee_count(self, obj):
        return obj.attendees.count()

    # Add other fields or methods as needed

    class Meta:
        model = Event
        fields = '__all__'


class DiscussionBoardSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    
    class Meta:
        model = DiscussionBoard
        fields = '__all__'  # Adjusted to include all fields for simplicity

class RSVPSerializer(serializers.ModelSerializer):
    event = EventSerializer(read_only=True)
    
    class Meta:
        model = RSVP
        fields = '__all__'  # Adjusted to include all fields for simplicity

class MovieCollectionSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    movies = MovieSerializer(many=True, read_only=True)
    
    class Meta:
        model = MovieCollection 
        fields = ['id', 'title', 'description', 'public', 'owner', 'movies', 'created_at', 'updated_at']