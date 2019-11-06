from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib import auth

from mesh_app.models import Profile

# Create your views here.

def register(req):
    if req.method == 'POST':
        first_name = req.POST['first_name']
        last_name = req.POST['last_name']
        username = req.POST['username']
        email = req.POST['email']
        password = req.POST['password']
        password2 = req.POST['password2']
        prof_pic = req.POST['prof_pic']
        field = req.POST['field']
        portfolio_link = req.POST['portfolio_link']
        linkedin = req.POST['linkedin']
        if password == password2:
            if User.objects.filter(username=username).exists():
                context = {'error':'Username is already taken'}
                return render(req, '')