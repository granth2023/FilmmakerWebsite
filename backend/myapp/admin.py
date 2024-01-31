from django.contrib import admin
from .models import Movie, User, Review, Event, Comment, DiscussionBoard, Like, RSVP 

admin.site.register(Movie) 
admin.site.register(User) 
admin.site.register(Review)
admin.site.register(Event) 
admin.site.register(Comment)
admin.site.register(DiscussionBoard)
admin.site.register(Like)
admin.site.register(RSVP) 
# Register your models here.
