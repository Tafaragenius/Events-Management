from django.db import models
from django.utils import timezone
from datetime import timedelta

class Register(models.Model):
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=15)
    surname = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=16)
    confirm_password = models.CharField(max_length=16)

    def __str__(self):
        return self.username

class Login(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=16)

    def __str__(self):
        return self.username

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    finish_time = models.DateTimeField()

    def __str__(self):
        return self.title