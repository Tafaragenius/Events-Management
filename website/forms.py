# forms.py

from django import forms
from .models import Register, Login, Event

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), label='Password')
    confirm_password = forms.CharField(widget=forms.PasswordInput(), label='Confirm Password')

    class Meta:
        model = Register
        fields = ['username', 'first_name', 'surname', 'email', 'password', 'confirm_password']
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match")

class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'start_time', 'finish_time']
        widgets = {
            'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'finish_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }