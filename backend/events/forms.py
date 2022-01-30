from django import forms
from django.forms import ModelForm
from .models import event

class event_form(ModelForm):
    model = event
    fields = ('event_name', 'event_description', 'event_date', 'event_end','registration_start', 'event_poster')
    labels = {
        'event_name': '',
        'event_description': '',
        'event_date': 'YYYY-MM-DD HH:MM:SS',
        'event_end': 'YYYY-MM-DD HH:MM:SS',
        'registration_start': 'YYYY-MM-DD HH:MM:SS',
        'event_poster': '',
    }
    widgets = {
        'event_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Event Name'}),
        'event_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Event Date'}),
        'event_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Event End'}),
        'registration_start': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Event Registration Data'}),
        'event_poster': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Event Poster'}),
        'event_description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
    }