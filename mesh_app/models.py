from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    prof_pic = models.TextField()
    field = models.CharField(max_length=100)
    portfolio_link = models.TextField()
    linkedin = models.TextField()

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
    
    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

class Event(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='events')
    title = models.CharField(max_length=100)
    date_time = models.DateTimeField()
    location = models.TextField(max_length=100)
    capacity = models.PositiveIntegerField()
    description = models.TextField(max_length=255)
    picture = models.TextField()
    field = models.CharField(max_length=100)
    facebook = models.TextField()
    twitter = models.TextField()
    instagram = models.TextField()
    
    def __str__(self):
        return f'{self.title} - {self.creator}'

class Attendees(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='attendees')
    attendee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='attendees')

class Friends(models.Model):
    friend1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friend2')
    friend2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friend1')