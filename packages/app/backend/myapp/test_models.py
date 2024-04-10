from django.test import TestCase
from django.contrib.auth.models import User
from .models import Movie, Review, MovieCollection, Event, DiscussionBoard, Comment, Like, RSVP
from datetime import date

class MovieModelTest(TestCase):
    def setUp(self):
        self.movie = Movie.objects.create(
            title="Test Movie",
            year="2022",
            released=date.today(),
            runtime="120 min",
            genre="Drama",
            director="John Doe",
            writers="John Doe",
            actors="John, Jane",
            plot="Test plot",
            country="USA",
            poster_url="http://example.com/poster.jpg"
        )

    def test_movie_creation(self):
        self.assertTrue(isinstance(self.movie, Movie))
        self.assertEqual(self.movie.__str__(), "Test Movie")

class ReviewModelTest(TestCase):
    def setUp(self):
        # Create a user for the review
        self.user = User.objects.create_user(username='testuser', password='12345')
        # Create a movie for the review
        self.movie = Movie.objects.create(
            title="Test Movie",
            year="2022",
            released=date.today(),
            runtime="120 min",
            genre="Drama",
            director="John Doe",
            writers="John Doe",
            actors="John, Jane",
            plot="Test plot",
            country="USA",
            poster_url="http://example.com/poster.jpg"
        )
        # Create the review itself
        self.review = Review.objects.create(
            movie=self.movie,
            user=self.user,
            text="Great movie!",
            rating=5
        )


# Add similar tests for MovieCollection, Event, DiscussionBoard, Comment, Like, RSVP

class MovieCollectionModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.movie_collection = MovieCollection.objects.create(title="Faves", owner=self.user)
        
    def test_collection_creation(self):
        self.assertEqual(self.movie_collection.owner, self.user)
        self.assertEqual(self.movie_collection.title, "Faves")
    # Implement setup and test methods similar to MovieModelTest
   

class EventModelTest(TestCase):
    def setUp(self):
        self.host_user =User.objects.create_user(username='hostuser', password='testpass123')
        self.movie = Movie.objects.create(title="Movie", year="2010", released=date.today(), runtime="148 min", genre="Action, Sci-Fi", director="Christopher Nolan")
        self.event = Event.objects.create(title="Movie Night: Movie", movie=self.movie, host=self.host_user, date=date.today())
        
    def test_event_creation(self):
        self.assertEqual(self.event.title, "Movie Night: Movie")
        self.assertEqual(self.event.host, self.host_user)
    # Implement setup and test methods similar to MovieModelTest
    pass

class DiscussionBoardModelTest(TestCase):
    # Implement setup and test methods similar to MovieModelTest
    pass

class CommentModelTest(TestCase):
    # Implement setup and test methods similar to MovieModelTest
    pass

class LikeModelTest(TestCase):
    # Implement setup and test methods similar to MovieModelTest
    pass

class RSVPModelTest(TestCase):
    # Implement setup and test methods similar to MovieModelTest
    pass

# Note: Ensure to create necessary objects in the setUp method for each test case as needed
