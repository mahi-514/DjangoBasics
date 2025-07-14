from django import forms
from .models import Event
from django.utils import timezone

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'date', 'time','description']

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get("date")
        time = cleaned_data.get("time")
        if date and time and (date < timezone.now().date()):
            raise forms.ValidationError("You cannot schedule events in the past.")
        return cleaned_data