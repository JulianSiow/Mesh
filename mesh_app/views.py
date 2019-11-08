from django.shortcuts import render, redirect
from django.core import serializers
from django.contrib.auth.decorators import login_required

from .models import User, Event
from .forms import EventForm
# Create your views here.

def landing (request):
    return render (request, 'landing.html')

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

def profile_page(request,pk):
    user = User.objects.get(id=pk)
    context = {"user": user}
    return render(request,'profile.html', context)

# @login_required
def event_create(request, pk):
    user = User.objects.get(id=pk)
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            # event.creator = user
            event.save()
            return redirect('event_page', pk = event.pk)
    else:
        form = EventForm()
    context = {'form': form, 'header':"Add an Event!"}
    return render(request,'event_form.html', context)

def event_browse(request):
    event = Event.objects.all()
    context = {"event": event}
    return render(request, '____', context)

def event_page(request,pk):
    event = Event.objects.get(id=pk)
    context = {"event": event}
    return render(request, 'event_detail.html', context)

@login_required
def event_edit(request, pk, event_pk):
    event = Event.objects.get(id=pk)
    if request.method == 'POST':
        form = Event(request.POST, instance= event)
        if form.is_valid():
            event = form.save()
            return redirect('____', pk= event.pk)
    else:
        form = Event()
    context = {'form': form,'header': "Edit this event"}
    return render(request, '_____', context)

@login_required
def profile_edit(request, pk):
    user = User.objects.get(id=pk)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance = request.user)
        profile_form = ProfileForm(request.POST, instance = request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('___')
        else:
            messages.error(request,_('Please correct the fields and submit again.'))
    else:
        user_form = UserForm(instance = request.user)
        profile_form = ProfileForm(instace = request.user.profile)
    return render(request, '____',{
        'user_form': user_form,
        'profile_form': profile_form
    })

def about_page (request):
    return render (request, 'about.html')


















