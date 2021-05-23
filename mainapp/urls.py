from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.home, name='main-home'),
    path('home/', views.home, name='main-home'),
    path('about/', views.about, name='main-about'),
    path('msg/', views.messaging, name='main-msg'),
]