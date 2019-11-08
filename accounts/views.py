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
                return render(req, 'sign_up.html', context)
            else: 
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password,
                    first_name=first_name,
                    last_name=last_name,
                )
                user.save()
                user.profile.prof_pic = prof_pic
                user.profile.field = field
                user.profile.portfolio_link = portfolio_link
                user.profile.linkedin = linkedin
                user.profile.save()

            return redirect('events')
        else:
            context = {'error':'Passwords do not match'}
            return render(req, 'sign_up.html', context)
    else:
        return render(req, 'sign_up.html')

def login(req):
    if req.method == 'POST':
        username = req.POST['username']
        password = req.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(req, user)
            return redirect('profile_page')
        else:
            context = {'error':'Username or password is incorrect, please try again.'}
            return render(req, 'landing.html', context)
    else:
        return render(req, 'landing.html')

def logout(req):
    auth.logout(req)
    return redirect('landing_page')
