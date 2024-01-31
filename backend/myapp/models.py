from django.db import models
from django.contrib.auth.hashers import make_password

from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# Create your models here.
class Project(models.Model):
    tite = models.CharField(max_length=200)
    script = models.FileField('/scripts', null=True, blank=True)
    createor_note = models.TextField()
    link = models.URLField(blank=True, null=True)
    password_access = models.BooleanField(default=False)
    comprabale_titles = models.TextField()
    access_password = models.CharField(max_length=128, blank=True) 
    def set_passowrd(self, raw_password):
        self.access_password = make_password(raw_password)
    def __str__(self):
        return self.title
    
    
class Movie(models.Model):
    title = models.CharField(max_length=200)
    year = models.CharField(max_length=4)
    released = models.DateField()
    runtime = models.CharField(max_length=30)
    genre = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    writers = models.TextField()
    actors = models.TextField()
    plot = models.TextField()
    country = models.CharField(max_length=100)
    poster_url = models.CharField(max_length=500, unique=True)