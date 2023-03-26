from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from playground.models import *
from django.contrib.auth import authenticate, login
# from playground.forms import ContactForm
from django.conf import settings
from django.contrib.auth import get_user_model
User = get_user_model()
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid username or password'
    else:
        error_message = None
    return render(request, 'login.html', {'error_message': error_message})

def home(request):
    return render(request, 'home_page.html')

def event_page(request):
    request_slug = request.path[12:]
    e = Event.objects.get(slug = request_slug)
    event_name = e.name
    event_description = e.description
    event_time = e.startTime
    event_state = e.state
    event_venue = e.venue
    event_image = e.image
    
    context = {
        'event_name': event_name,
        'event_description': event_description,
        'event_time': event_time,
        'event_state': event_state,
        'event_venue': event_venue,
        'event_image': event_image 
    }
    
    return render(request, 'event_page.html', context)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # username = form.cleaned_data['username']
            # email = form.cleaned_data['email']
            # password = form.cleaned_data['password']
            # first_name = form.cleaned_data['first_name']
            # last_name = form.cleaned_data['last_name']
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email']
                # password=password,
                # first_name=first_name,
                # last_name=last_name,
            )
            
            
            return render(request, 'home.html')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


