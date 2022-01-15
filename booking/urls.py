from django.urls import path
from . import views

irlpatterns = [
    path('', views.index, name='index')
]