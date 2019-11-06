from django.shortcuts import render, redirect
from django.core import serializers
from django.contrib.auth.decorators import login_required

from .models import User, Event
# Create your views here.
