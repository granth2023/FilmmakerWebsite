from rest_framework.test import APITestCase, APIClient 
from django.urls import reverse 

from rest_framework import status  
from myapp.models import Movie, CustomUser, Event, MovieCollection, DiscussionBoard, MovieCollection, Comment, Like, RSVP
from rest_framework.authtoken.models import Token  
from django.contrib.auth import get_user_model
User = get_user_model()

class APITests(APITestCase):
    
    def setUp(self):
        
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client= APIClient()
        self.client.force_authenticate(user=self.user)
        
        self.movie = Movie.objects.create(title='Test Movie', year='2024')
        self.movie_collection = MovieCollection.objects.create(title="test collection", owner = self.user)
        self.event = Event.objects.create(title='Test event', host=self.user)
        self.comment = Comment.objects.create(discussion_board_id=1, user=self.user, test="test comment")
        self.rsvp = RSVP.objects.create(event=self.event, user=self.user, status='yes')
        
        
    def test_movie_list(self):
        url = reverse('movie-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_movie_collection(self):
        url = reverse('movie-collection')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_event_list_get(self):
        url = reverse('events-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)    
        
    def test_event_rsvp(self):
        url = reverse('event-rsvp', kwargs={'pk': self.event.pk})        
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_comment_list_get(self):
        url = reverse('comment-lists')
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_rsvp_list_get(self):
        url = reverse('rsvp-list')
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_discussionboard_list_get(self):
        url = reverse('discussion-board-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def tearDown(self):
        self.user.delete()
        self.movie.delete()
        self.movie_collection.delete()
        self.event.delete()
        self.comment.delete()
        self.rsvp.delete()
      
        
        
if __name__ == '__main__':
    APITestCase.main()