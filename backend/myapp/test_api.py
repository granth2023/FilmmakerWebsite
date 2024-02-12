from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User 
from .models import Movie, Review 

class UserAccountTests(APITestCase):
    
    def test_user_registration(self):
        """ 
        Ensure we can create a new user account 
        """
        url = reverse('register')
        data = {'username': 'testuser', 'email': 'testuser@example.com', 'password': 'testpassword'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue('access' in response.data)
        self.assertTrue('refrresh' in response.data)    
    
    def test_user_login(self):
        """" 
        Ensure we cna log a user in 
        """
        
        self.test_user_registration() 
        
        url = reverse('login')
        data = {'username': 'testuser', 'password': 'testpassword'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('access' in response.data)
        

class MovieTests(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)        
        
    def test_create_movie(self):
        """"
        Ensure we can create a new movie object
        """
        url = reverse('movie-list')
        data = {'title': 'Test Movie', 'year': '2020', 'genre': 'Drama'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Movie.objects.count(), 1)
        self.assertEqual(Movie.objects.get().title, 'Test Movie')
                
    
    def test_get_movies(self):
        """
        Ensure we cna retrieve movies
        """
        
        self.test_create_movie()
        url = reverse('movie-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK) 
        self.assertEqual(len(response.data), 1)
        