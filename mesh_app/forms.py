from django import forms
from .models import User, Event, Profile

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('title', 'date_time', 'location', 'capacity', 'description', 'picture', 'field', 'facebook', 'twitter', 'instagram')
        

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('prof_pic', 'field', 'portfolio_link', 'linkedin')