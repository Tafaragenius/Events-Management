from django.urls import path
from . import views 
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('events/', views.event_list, name='event_list'),
    path('add_event/', views.add_event, name='add_event'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('events/edit/<int:event_id>/', views.edit_event, name='edit_event'),
    path('events/delete/<int:event_id>/', views.delete_event, name='delete_event'),
    
    path('events/add/', views.add_event, name='add_event'),
    path('events/edit/<int:event_id>/', views.edit_event, name='edit_event'),
    path('events/delete/<int:event_id>/', views.delete_event, name='delete_event'),  # Assuming you have a delete_event view
    path('logout/', views.logout_view, name='logout'),  # Assuming you have a logout_view
]


