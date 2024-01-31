from rest_framework import serializers
from .models import Movie, Review, Event, DiscussionBoard, Comment, User, RSVP, MovieCollection

# Assuming your User model customization is correct, just correcting the serializer name and fields
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'profile_picture']  # Assuming the field is 'profile_picture'

class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Review
        fields = ['id', 'user', 'text', 'rating', 'created_at']

# Corrected base class and included reviews properly
class MovieSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)  # Ensure your Movie model has a reverse relation to Review that allows this
    
    class Meta:
        model = Movie
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'  # Adjusted to include all fields for simplicity

class EventSerializer(serializers.ModelSerializer):
    attendees = UserSerializer(many=True, read_only=True)
    invitees = UserSerializer(many=True, read_only=True)
    
    class Meta:
        model = Event
        fields = '__all__'  # Adjusted to include all fields for simplicity

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
    
    class Meta:
        model = MovieCollection 
        fields = ['id', 'title', 'description', 'public', 'owner', 'movies', 'created_at', 'updated_at']