from django import forms
from .models import User, Event

class Event(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('title', 'date', 'location', 'capacity', 'description', 'picture', 'field', 'facebook', 'twitter', 'instagram')
        

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'password','confirm_password', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('prof_pic', 'field', 'portfolio_link', 'linkedin')