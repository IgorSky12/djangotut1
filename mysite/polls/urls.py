from django.urls import path
from . import views

urlplatterns = [
    path('', views.index, name='index'),
]