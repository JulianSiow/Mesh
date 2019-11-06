from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    prof_pic = models.TextField()
    field = models.CharField(max_length=100)
    portfolio_link = models.TextField()
    events = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='creator')

    @reciever(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
    
    @reciever(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


class Event(models.Model):
    title = models.CharField(max_length=100)
    date_time = models.DateTimeField()
    location = models.TextField(max_length=100)
    capacity = models.PositiveIntegerField()
    description = models.TextField(max_length=255)
    picture = models.TextField()
    field = models.CharField(max_length=100)
    attendees = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.title} - {self.user}'

