from django.urls import path

from .views import *

urlpatterns = [
    path('MainPage/',index, name = "MainPage"),
    path('Rooms/',rooms, name = "Rooms"),
    path('Booking/',booking, name = "Booking"),
    path('About/',about, name = "About"),
]