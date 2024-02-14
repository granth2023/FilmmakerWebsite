from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Movie

class UserAccountTests(APITestCase):

    def test_user_registration(self):
        """
        Ensure we can create a new user account
        """
        url = reverse('register')  # This should match the name in your urlpatterns
        data = {'username': 'testuser', 'email': 'testuser@example.com', 'password': 'testpassword'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue('access' in response.data)
# Corrected typo here

    def test_user_login(self):
        """Ensure we can log a user in"""
        self.test_user_registration()

        url = reverse('login')
        data = {'username': 'testuser', 'password': 'testpassword'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('access' in response.data)

# class MovieTests(APITestCase):

#     def setUp(self):
#         super().setUp()
#         self.user = User.objects.create_user(username='testuser', password='testpassword')
      

#     def test_create_movie(self):
#         """Ensure we can create a new movie object"""
#         url = reverse('movie-list')
#         data = {
#             'title': 'Test Movie',
#             'year': '2022',  # Ensure all required fields are included
#             'released': '2022-01-01',
#             'runtime': '120 min',
#             'genre': 'Drama',
#             'director': 'John Doe',
#             'writers': 'John Doe, Jane Doe',
#             'actors': 'Actor 1, Actor 2',
#             'plot': 'This is a test plot.',
#             'country': 'Testland',
#             'poster_url': 'http://example.com/poster.jpg'
#         }
#         self.client.login(username='testuser', password='testpassword')
#         response = self.client.post(url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(Movie.objects.count(), 1)
#         self.assertEqual(Movie.objects.get().title, 'Test Movie')

#     def test_get_movies(self):
#         """Ensure we can retrieve movies"""
#         self.test_create_movie()  # This creates a dependency between tests, consider using setUp()
#         url = reverse('movie-list')
#         response = self.client.get(url, format='json')

#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(len(response.data), 1)
