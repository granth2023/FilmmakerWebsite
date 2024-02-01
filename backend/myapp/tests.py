from django.test import TestCase
from .models import Movie, MovieCollection, Event, User, Comment, DiscussionBoard, Like, RSVP, Review
# Create your tests here.


class MovieModel(TestCase):
    @classmethod
    def setUpTestData(cls):
        
        Movie.objects.create(title='Titanic', year='1997')
        
    def test_title_content(self):
        movie = Movie.objects.get(id=1)
        expected_object_name = f'{movie.title}'
        self.assertEquals(expected_object_name, 'Titanic')
        
class ReviewModelTest(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='testuser', password='12345')
        movie = Movie.objects.create(title="Inception", year='2010')
        Review.objects.create(movie=movie, user=user, text='Great Movie!', rating=9)
        
    def test_review_content(self):
        review = Review.objects.get(id=1)
        expected_object_text = f'{review.text}'
        self.assertEqual(expected_object_text, 'Great Movie!')
        
        
class MovieCollection(TestCase):
    @classmethod
    def setUpTestData(cls): 
        cls.user = User.objects.create_user(username='collection_owner', password='12345')
        cls.movie_collection = MovieCollection.objects.create(title="Sci-Fi Collection", description="Sci-Fi Collection", owner=cls.user)
        
    def test_str_representation(self):
        self.assertEqual(srt(self.movie_collection), "Sci-Fi Collection")
        
class EventModelTest(TestCase):
    @classmethod