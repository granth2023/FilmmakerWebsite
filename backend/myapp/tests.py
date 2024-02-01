from django.test import TestCase
from .models import Movie, MovieCollection, Event, User, Comment, DiscussionBoard, Like, RSVP 
# Create your tests here.


class MovieModel(TestCase):
    @classmethod
    def setUpTestData(cls):
        
        Movie.objects.create(title='Titanic', year='1997')
        
    def test_title_content(self):
        movie = Movie.objects.get(id=1)
        expected_object_name = f'{movie.title}'
        self.assertEquals(expected_object_name, 'Titanic')