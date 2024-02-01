from django.test import TestCase
from django.test import cls
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
        self.assertEqual(str(self.movie_collection), "Sci-Fi Collection")
        
class EventModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='event_host', password='12345')
        cls.event = Event.objects.create(title="Movie Night", host=cls.user)
        
    def test_str_representation(self):
        self.assertEqual(str(self.event), "Movie Night")
        
class DiscussionBoardModelTest(TestCase):
    @classmethod
    def setUpTestData(cls): 
        cls.event = Event.objects.create(title="Movie Night")
        cls.discussion_board = DiscussionBoard.objects.create(event=cls.event)
        
    def test_str_representation(self):
        self.assertEqual(str(self.discussion_board), f"discussion_board for {cls.event}")
        
class CommentModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user =User.objects.create_user(username='comment_user', password='12345')
        cls.discussion_board = DiscussionBoard.objects.create() 
        cls.comment = Comment.objects.create(discussion_board=cls.discussion_board, user=cls.user, text="interesting topic!")
        
    def test_str_representation(self):
        self.assertEqual(str(self.comment), f"comment by {cls.user.username}")
        
class LikeModelTest(TestCase):
    @classmethod
    def setUptestData(cls):
        cls.user = User.objects.create_user(username='liker', password='12345')
        cls.comment = Comment.objects.create(text="interesting topic!")
        cls.like = Like.objects.create(user=cls.user, comment=cls.comment )
        
    def test_str_representation(self):
        self.assertEqual(str(self.like), f"like by {cls.user.username} on comment {cls.comment.id}")
        
class RSVPModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='rsvp_user', password='12345')
        cls.event = Event.objects.create(title='Movie Night')
        cls.rsvp = RSVP.objects.create(event=cls.event, user=cls.user, status='yes')
        
    def test_str_representation(self):
        self.assertEqual(str(self.rsvp), f'rsvp by {cls.user.username}')
        
if __name__ == '__main__':
    TestCase.main()