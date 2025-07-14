from django.test import TestCase
from django.contrib.auth.models import User
from .models import Event

class EventModelTest(TestCase):
    def test_event_creation(self):
        user = User.objects.create_user(username='testuser', password='12345')
        event = Event.objects.create(
            user=user,
            name='Test Event',
            date='2025-12-31',
            time='18:00',
            description='End of year test'
        )
        self.assertEqual(event.name, 'Test Event')