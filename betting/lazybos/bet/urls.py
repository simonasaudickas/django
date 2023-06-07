#from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('mygtukas/', views.say_hello),
    path('forma/', views.simple_form),
    path('komanda/', views.komanda, name='komanda'),
    path('article/', views.article, name='straipsniai'),

]
