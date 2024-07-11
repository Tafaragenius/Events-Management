from django.urls import path
from . import views 
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('events/', views.event_list, name='event_list'),
    path('add_event/', views.add_event, name='add_event'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]