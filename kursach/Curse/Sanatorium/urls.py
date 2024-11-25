
from django.urls import path

from .views import *

urlpatterns = [
    path('mainpage/', index, name = "mainpage"),
    path('rooms/', rooms, name = "rooms"),
    path('booking/', booking, name = "booking"),
    path('about/', about, name = "about"),
    path('rooms/<slug:room_slug>', show_room, name = "room"),
    path('addusers/',addusers, name = 'addusers')
]