from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Movie, Review, Event

User = get_user_model()

class UserModelTest(TestCase):
    def test_user_creation(self):
        user = User.objects.create_user(email='user@example.com', password='testpass')
        self.assertEqual(user.email, 'user@example.com')"
    "
    
    
class MovieModelTest(TestCase):
    

class EventModelTest(TestCase):