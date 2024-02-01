from rest_framework.test import APITestCase, APIClient 
from django.urls import reverse 

from rest_framework import status  
from django.contrib.auth.models import Movie, User, Event, MovieCollection, DiscussionBoard, MovieCollection, Comment, Like, RSVP
from rest_framework.authtoken.models import Token  


class APITests(APITestCase):
    
    def setUp(self):
        
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client= APIClient()
        self.client.force_authenticate(user=self.user)
        
        self.movie = Movie.objects.create(title='Test Movie', year='2024')
        self.movie_collection = MovieCollection.objects.create(title="test collection", owner = self.user)
        self.event = Event.objects.create(title='Test event', host=self.user)
        
    def test_movie_list(self):
        url = reverse('movie-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_movie_collection(self):
        url = reverse('movie-collection')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_event_rsvp(self):
        url = reverse('event-rsvp', kwargs={'pk': self.event.pk})        
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_comment(self):
        url = reverse('comment', kwargs={'pk': self.comment.pk})
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def tearDown(self):
        self.user.delete()
        self.movie.delete()
        self.movie_collection.delete()
        self.event.delete()
      
        
        
if __name__ == '__main__':
    APITestCase.main()