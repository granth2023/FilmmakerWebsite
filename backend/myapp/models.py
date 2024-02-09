from django.conf import settings

from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.validators import MinValueValidator, MaxValueValidator



from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class Profile(models.Model):
    user =  models.OneToOneField(User, on_delete=models.CASCADE)
    
    

# Create your models here.
# class Project(models.Model):
#     tite = models.CharField(max_length=200)
#     script = models.FileField('/scripts', null=True, blank=True)
#     createor_note = models.TextField()
#     link = models.URLField(blank=True, null=True)
#     password_access = models.BooleanField(default=False)
#     comprabale_titles = models.TextField()
#     access_password = models.CharField(max_length=128, blank=True) 
#     def set_passowrd(self, raw_password):
#         self.access_password = make_password(raw_password)
#     def __str__(self):
#         return self.title
    
    
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
    
    def __str__(self):
        return self.title
    

        
class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)
    
class MovieCollection(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    public = models.BooleanField(default=True)
    owner = models.ForeignKey(User, related_name='movie_collections', on_delete=models.CASCADE)
    movies = models.ManyToManyField(Movie, related_name='collections')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class Event(models.Model):
    title = models.CharField(max_length=200)
    movie = models.ForeignKey(Movie,  on_delete=models.CASCADE)
    host = models.ForeignKey(User, related_name='hosted_events', on_delete=models.CASCADE)
    date = models.DateTimeField()
    invitees = models.ManyToManyField(User, related_name='invited_events')
    attendees = models.ManyToManyField(User, related_name='attended_events')
    location = models.CharField(max_length=200, null=True, blank=True)
    virtual_event_link=models.URLField(max_length=500, null=True, blank=True)
    collection = models.ForeignKey( MovieCollection, related_name='events', on_delete=models.SET_NULL, null=True, blank=True)
    # CustomUser = models.ForeignKey(CustomUser, related_name='events')
class DiscussionBoard(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey( 'content_type', 'object_id')
    event = models.OneToOneField(Event, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    moderators = models.ManyToManyField(User, related_name = 'moderated_boards')
    
    
    def __str__(self):
        return f'Discussion Board for {self.content_object}'
    
    
class Comment(models.Model):
    discussion_board = models.ForeignKey(DiscussionBoard, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie,  on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')
    likes = models.ManyToManyField(User, related_name='liked_comments')
    
    def get_children(self):
        return Comment.objects.filter(parent=self) 
    
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Like by {self.user.username} on comment {self.comment.id}'


class RSVP(models.Model):
    event = models.ForeignKey('Event', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # other fields...

    status = models.CharField(max_length=10, choices=[('yes', 'Yes'), ('no', 'No'), ('maybe', 'Maybe')])
    
    def __str__(self):
        return f'RSVP by {self.user.usernanme} for {self.event.title} as {self.status}'
    

#CL: PSQL -> \c sscc 

#test