from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('next', views.next, name='next'),
    path('next2', views.next2, name='next2'),
    path('next3', views.next3, name='next3')

]