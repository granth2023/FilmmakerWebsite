# from django.test import TestCase
# from .models import Movie, MovieCollection, Event, Comment, DiscussionBoard, Like, RSVP, Review
# from django.contrib.auth import get_user_model
# User = get_user_model()

# class MovieModelTest(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         cls.movie = Movie.objects.create(title='Titanic', year='1997')
        
#     def test_title_content(self):
#         expected_object_name = f'{self.movie.title}'
#         self.assertEquals(expected_object_name, 'Titanic')

# class ReviewModelTest(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         cls.user = User.objects.create_user(username='testuser', password='12345')
#         cls.movie = Movie.objects.create(title="Inception", year='2010')
#         cls.review = Review.objects.create(movie=cls.movie, user=cls.user, text='Great Movie!', rating=9)

#     def test_review_content(self):
#         expected_object_text = f'{self.review.text}'
#         self.assertEqual(expected_object_text, 'Great Movie!')

# class MovieCollectionTest(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         cls.user = User.objects.create_user(username='collection_owner', password='12345')
#         cls.movie_collection = MovieCollection.objects.create(title="Sci-Fi Collection", description="A collection of Sci-Fi movies", owner=cls.user)

#     def test_str_representation(self):
#         self.assertEqual(str(self.movie_collection), "Sci-Fi Collection")

# class EventModelTest(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         cls.user = User.objects.create_user(username='event_host', password='12345')
#         cls.event = Event.objects.create(title="Movie Night", host=cls.user)

#     def test_str_representation(self):
#         self.assertEqual(str(self.event), "Movie Night")

# class DiscussionBoardModelTest(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         cls.event = Event.objects.create(title="Movie Night")
#         cls.discussion_board = DiscussionBoard.objects.create(event=cls.event)

#     def test_str_representation(self):
#         self.assertEqual(str(self.discussion_board), f"Discussion Board for {self.event}")

# class CommentModelTest(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         cls.user = User.objects.create_user(username='comment_user', password='12345')
#         cls.discussion_board = DiscussionBoard.objects.create()
#         cls.comment = Comment.objects.create(discussion_board=cls.discussion_board, user=cls.user, text="Interesting topic!")

#     def test_str_representation(self):
#         self.assertEqual(str(self.comment), f"Comment by {self.user.username}")

# class LikeModelTest(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         cls.user = User.objects.create_user(username='liker', password='12345')
#         cls.comment = Comment.objects.create(text="Interesting topic!")
#         cls.like = Like.objects.create(user=cls.user, comment=cls.comment)

#     def test_str_representation(self):
#         self.assertEqual(str(self.like), f"Like by {self.user.username} on comment {self.comment.id}")

# class RSVPModelTest(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         cls.user = User.objects.create_user(username='rsvp_user', password='12345')
#         cls.event = Event.objects.create(title='Movie Night')
#         cls.rsvp = RSVP.objects.create(event=cls.event, user=cls.user, status='yes')

#     def test_str_representation(self):
#         self.assertEqual(str(self.rsvp), f'RSVP by {self.user.username} for {self.event.title} as {self.rsvp.status}')

# if __name__ == '__main__':
#     TestCase.main()
#TEST TEST 