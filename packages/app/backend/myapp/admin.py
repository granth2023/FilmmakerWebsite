from django.contrib import admin
from .models import Movie, Review, Event, Comment, DiscussionBoard, Like, RSVP 
from django.contrib.auth import get_user_model
User = get_user_model()

admin.site.register(Movie) 

admin.site.register(Review)
admin.site.register(Event) 
admin.site.register(Comment)
admin.site.register(DiscussionBoard)
admin.site.register(Like)
admin.site.register(RSVP) 
# Register your models here.
