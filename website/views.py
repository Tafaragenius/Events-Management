from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, RegisterForm, EventForm
from django.contrib import messages
from django.utils import timezone
from .models import Register, Event

from django.contrib.auth import authenticate, login as auth_login
from .forms import LoginForm

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('event_list')  # Redirect to the events page after login
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('event_list')  # Redirect to events page
            else:
                messages.error(request, 'Invalid username or password')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            first_name = form.cleaned_data.get('first_name')
            surname = form.cleaned_data.get('surname')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            # Create the user
            Register.objects.create(
                username=username,
                first_name=first_name,
                surname=surname,
                email=email,
                password=password
            )
            messages.success(request, 'Registration successful. Please log in.')
            return redirect('login')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Event added successfully!')
            return redirect('event_list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = EventForm()
    return render(request, 'add_event.html', {'form': form})

def event_list(request):
    events = Event.objects.all().order_by('-start_time')  # Order by start_time descending
    now = timezone.now()
    return render(request, 'events.html', {'events': events, 'now': now})