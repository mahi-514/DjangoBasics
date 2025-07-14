from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from.models import Event
from .forms import EventForm
from django.core.mail import send_mail
from django.utils.timezone import now
from .models import Event
from django.contrib.auth.models import User

@login_required
def event_list(request):
    events = Event.objects.filter(user=request.user)
    return render(request, 'events/event_list.html', {'events': events})

@login_required
def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk, user=request.user)
    return render(request, 'events/event_detail.html', {'event': event})

@login_required
def event_create(request):
    form = EventForm(request.POST or None)
    if form.is_valid():
        event = form.save(commit=False)
        event.user = request.user
        event.save()
        return redirect('event_list')
    return render(request, 'events/event_form.html', {'form': form})

@login_required
def event_update(request, pk):
    event = get_object_or_404(Event, pk=pk, user=request.user)
    form = EventForm(request.POST or None, instance=event)
    if form.is_valid():
        form.save()
        return redirect('event_list')
    return render(request, 'events/event_form.html', {'form': form})

@login_required
def event_delete(request, pk):
    event = get_object_or_404(Event, pk=pk, user=request.user)
    if request.method == 'POST':
        event.delete()
        return redirect('event_list')
    return render(request, 'events/event_confirm_delete.html', {'event': event})

@login_required
def send_event_reminders():
    upcoming_events = Event.objects.filter(date=now().date())
    for event in upcoming_events:
        send_mail(
            subject=f'Reminder: {event.name}',
            message=f'Dear {event.user.username},\n\nThis is a reminder for your event: {event.name} at {event.time}.\n\nDetails: {event.description}',
            from_email='mahinbamb@gmail.com',
            recipient_list=[event.user.email],
            fail_silently=False,
        )