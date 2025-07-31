from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_thought, name='create_thought'),
    path('', views.home, name='home'),
]