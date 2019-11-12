from django.shortcuts import render, redirect
from django.core import serializers
from django.contrib.auth.decorators import login_required

from .models import User, Event, Attendees
from .forms import EventForm, UserForm, ProfileForm
# Create your views here.

#---------------------------Landing Page----------------------------------

def landing (request):
    return render (request, 'landing.html')

#---------------------------Profile Routes--------------------------------

@login_required
def profile_page(request):
    user = request.user
    my_events = Attendees.objects.filter(attendee=user)
    context = {"user": user,"my_events": my_events}
    return render(request,'profile.html', context)

@login_required
def profile_edit(request, pk):
    user = User.objects.get(id=pk)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance = request.user)
        profile_form = ProfileForm(request.POST, instance = request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.profile = profile_form.save()
            return redirect('user')
        else:
            messages.error(request,_('Please correct the fields and submit again.'))
    else:
        user_form = UserForm(instance = request.user)
        profile_form = ProfileForm(instance = request.user.profile)
    return render(request, 'profile_form.html',{
        'user_form': user_form,
        'profile_form': profile_form
    })

#---------------------------Event Routes-------------------------------------

def event_browse(request):
    event = Event.objects.all()
    context = {"event": event}
    return render(request, 'event_browse.html', context)

def event_page(request, event_pk):
    event = Event.objects.get(id=event_pk)
    user = request.user
    attending = Attendees.objects.filter(event=event, attendee=user).exists()
    if user == event.creator:
        delete_available = True
    else:
        delete_available = False
    context = {"event":event, "attending":attending, "delete_available":delete_available}
    return render(request, 'event_detail.html', context)

@login_required
def event_create(request, pk):
    user = request.user
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.creator = user
            event.save()
            return redirect('event_page', event_pk=event.pk)
    else:
        form = EventForm()
    context = {'form': form, 'header':"Add an Event!"}
    return render(request,'event_form.html', context)

@login_required
def event_join(request, event_pk, pk):
    user = User.objects.get(id=pk)
    event = Event.objects.get(id=event_pk)
    if Attendees.objects.filter(event=event, attendee=user).exists():
        Attendees.objects.get(event=event, attendee=user).delete()
    else:
        user_join = Attendees(event=event, attendee=user)
        user_join.save()
    context = {"event": event}
    return redirect('event_page', event_pk=event_pk)

@login_required
def event_edit(request, event_pk):
    user = request.user
    event = Event.objects.get(id=event_pk)
    if request.method == 'POST':
        form = EventForm(request.POST, instance = event)
        if form.is_valid():
            event = form.save()
            return redirect('event_page', event_pk=event.pk)
    else:
        form = EventForm(instance = event)
    context = {'form':form, 'event':event, 'header':"Edit this event"}
    return render(request, 'event_form.html', context)

@login_required
def event_delete(request, event_pk):
    user = request.user
    event = Event.objects.get(id=event_pk)
    if event.creator == user:
        event.delete()
        return redirect('user')
    else:
        return redirect('landing')

#--------------------------About Route---------------------------------

def about_page (request):
    return render (request, 'about.html')


















