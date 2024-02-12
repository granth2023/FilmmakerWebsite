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
        

class MovieTests(APITestCase):
    
    def setUp(self):
        
        
    def test_create_movie(self):
        
    
    def test_get_movies(self):