from django.shortcuts import render, redirect
from django.core import serializers
from django.contrib.auth.decorators import login_required

from .models import User, Event
# Create your views here.

def profile_create(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save()
            return redirect('____', pk=profile.pk)
    else:
        form = ProfileForm()
    context = {'form': form}
    return render(request, '____', context)

def event_create(request):
    user = User.object.get(id=pk)
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valud():
            event = form.save(commit=False)
            event.creator = user
            return redirect('____', pk = event.pk)
        else:
            form = EventForm()
        context = {'form': form, 'header':"Add an Event!"}
        return render(request,'____', context)


