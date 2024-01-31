from django.shortcuts import render
from rest_framework import Project 
from .models import Project 
from .serializers import ProjectSerializer
from rest_framework import generics
import requests  
import django.conf import settings
from django.http import JsonResponse
# Create your views here.
class ProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer