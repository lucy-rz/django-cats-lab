from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    #new path to 'about/' that goes to views about
    path('about/', views.about),
    path('cats/', views.cats_index),
]