from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.camera, name='camera'),
    path('signup', views.signup, name='signup'),
]