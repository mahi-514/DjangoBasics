from celery import shared_task

@shared_task
def send_event_reminder():
    print("Reminder sent")

@shared_task
def generate_report():
    print("Report generated")
