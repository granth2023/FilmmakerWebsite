from django.shortcuts import render
from rest_framework import Project 
from .models import Project 
from .serializers import ProjectSerializer
# Create your views here.
class ProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.all()