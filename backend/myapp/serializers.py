from rest_framework import serializers
from .models import Movie 


class ProjectSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Movie 
        fields ='__all__'
        
        