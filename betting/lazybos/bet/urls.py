#from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('forma/', views.simple_form),
    path('komanda/', views.komanda, name='komanda'),
    path('article/', views.article, name='straipsniai'),
    path('test/', views.test, name='testavimas'),
    path('contact/', views.contact, name='susisiekti'),
    path('success/', views.success, name='susiekta'),
    path('paslaugos/', views.paslaugos, name='paslaugos'),

]
