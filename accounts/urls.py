# accounts/urls.py
from django.urls import path
from .views import register_view, custom_login_view, logout_view, newsfeed_view

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', custom_login_view, name='login'),
    path('newsfeed/', newsfeed_view, name='newsfeed'),  # Placeholder for newsfeed view
    path('logout/', logout_view, name='logout'),
]
