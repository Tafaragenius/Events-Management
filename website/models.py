from django.db import models
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.conf import settings


class CustomUserManager(BaseUserManager):
    def create_user(self, email, first_name, surname, password=None):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, surname=surname)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, surname, password=None):
        user = self.create_user(email, first_name, surname, password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=15)
    surname = models.CharField(max_length=15)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'surname']

    def __str__(self):
        return self.email

class Event(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    finish_time = models.DateTimeField()
    venue = models.CharField(max_length=200)

    def __str__(self):
        return self.title

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
