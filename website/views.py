from django.shortcuts import render,get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RegisterForm, EventForm
from django.contrib import messages
from django.utils import timezone
from .models import Register, Event
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login as auth_login
from .forms import LoginForm


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('event_list')
        else:
            messages.error(request, 'Invalid email or password')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful. Please log in.')
            return redirect('login')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('event_list')
            else:
                form.add_error(None, 'Invalid email or password')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def event_list(request):
    events = Event.objects.all().order_by('-start_time')
    return render(request, 'events.html', {'events': events})

@login_required
def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user
            event.save()
            messages.success(request, 'Event added successfully!')
            return redirect('event_list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = EventForm()
    return render(request, 'add_event.html', {'form': form})

@login_required
def edit_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    if event.user != request.user:
        messages.error(request, 'You are not authorized to edit this event.')
        return redirect('event_list')
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, 'Event updated successfully!')
            return redirect('event_list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = EventForm(instance=event)
    return render(request, 'edit_event.html', {'form': form})

@login_required
def delete_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if event.user == request.user:
        event.delete()
        messages.success(request, 'Event deleted successfully!')
    else:
        messages.error(request, 'You are not authorized to delete this event.')
    return redirect('event_list')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')