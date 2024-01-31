from rest_framework import serializers
from .models import Movie, Review, Event, DiscussionBoard, Comment, Like, RSVP 


class ProjectSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Movie 
        fields ='__all__'
        
class ReviewSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Review 
        fields = '__all__'
        
class CommentSerializer(serializers.ModelSerializer):
    class Meta: 
        model: Comment
        fields = '__all__'
        
class EventSerializer(serializers.ModelSerializer):
    class Meta: 
        model: Event
        fields = '__all__'
        
class DiscussionBoardSerializer(serializers.DicussionBoardSerializer):
    class Meta: 
        model: DiscussionBoard
        fields = '__all__'
        
class RSVPSerializer(serializers.RSVPSerializer):
    class Meta: 
        model: RSVP 
        fields = '__all__'