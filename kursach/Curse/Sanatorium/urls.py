from django.urls import path

from .views import *

urlpatterns = [
    path('mainpage/', index, name="mainpage"),
    path('rooms/', Rooms.as_view(), name="rooms"),
    path('program/', booking, name="programs"),
    path('program/<slug:program_slug>',show_program, name = "program"),
    path('about/', about, name="about"),
    path('rooms/<slug:room_slug>', show_room, name="room"),
    path('addusers/', addusers, name='addusers'),
    path('food/', food, name = 'food')
]
