from django.contrib import admin
from django.urls import path, include

from blog import views

urlpatterns = [
    path('', views.home, name='home-blog'),
    path('about/', views.about, name='about-blog'),
]
