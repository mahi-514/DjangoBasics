import os
from celery import Celery
from kombu import Queue

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'event_scheduler.settings')

app = Celery('event_scheduler')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# Define named queues using kombu.Queue
app.conf.task_queues = (
    Queue('reminder_queue'),
    Queue('report_queue'),
)

app.conf.task_routes = {
    'events.tasks.send_event_reminder': {'queue': 'reminder_queue', 'routing_key': 'reminder'},
    'events.tasks.generate_report': {'queue': 'report_queue', 'routing_key': 'report'},
}