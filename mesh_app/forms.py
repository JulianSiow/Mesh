from django import forms
from .models import User, Event

class Event(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('title', 'date', 'location', 'capacity', 'description', 'picture', 'field', 'facebook', 'twitter', 'instagram')
        