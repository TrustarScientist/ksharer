from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_thought, name='create_thought'),
    path('', views.home, name='home'),
    path('thoughts/<int:thought_id>/upload-images/', views.upload_thought_images, name='upload_thought_images'),
]