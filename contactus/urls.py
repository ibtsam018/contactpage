from django.urls import path
from django.contrib import admin
from .views import feedback

app_name = 'contactus'
urlpatterns = [
     path('', feedback, name='contactus'),
]
