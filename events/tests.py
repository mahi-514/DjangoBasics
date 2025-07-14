from django.test import TestCase
from django.contrib.auth.models import User
from .models import Event
from .tasks import send_event_reminder
from django.utils import timezone
from datetime import timedelta

class EventModelTest(TestCase):
    def test_event_creation(self):
        user = User.objects.create_user(username='mahi.bamb', password='12345')
        event = Event.objects.create(
            user=user,
            name='Test Event',
            date='2025-12-31',
            time='18:00',
            description='End of year test'
        )
        self.assertEqual(event.name, 'Test Event')

class CeleryReminderTest(TestCase):
    def test_send_reminder_task(self):
        user = User.objects.create_user(username='mahi.bamb', email='mahinbamb@gmail.com', password='12345')
        Event.objects.create(
            name='Reminder Test Event',
            user=user,
            date=timezone.now().date() + timedelta(days=1),
            time=timezone.now().time(),
            description='Reminder event'
        )
        send_event_reminder()  
