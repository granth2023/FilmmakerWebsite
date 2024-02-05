from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Movie, Review, Event

User = get_user_model()

class UserModelTest(TestCase):
    def test_user_creation(self):
        user = User.objects.create_user(email='user@example.com', password='testpass')
        self.assertEqual(user.email, 'user@example.com')
    
    
class MovieModelTest(TestCase):
    def setUp(self):
        Movie.objects.create(title="Titanic", year="1997", director="James Cameron")
    
    def test_movie_creation(self):
        movie = Movie.objects.get(title="Titanic")
        self.assertEqual(movie.year, "1997")
    

class EventModelTest(TestCase):