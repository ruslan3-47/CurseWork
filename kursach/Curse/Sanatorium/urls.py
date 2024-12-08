from django.urls import path

from .views import *

urlpatterns = [
    path('mainpage/', Homepage.as_view(), name="mainpage"),
    path('rooms/', Rooms.as_view(), name="rooms"),
    path('program/', Program_html.as_view(), name="programs"),
    path('program/<slug:program_slug>',Show_program.as_view(), name = "program"),
    path('about/', About.as_view(), name="about"),
    path('rooms/<slug:room_slug>', ShowRoom.as_view(), name="room"),
    path('addusers/', addusers, name='addusers'),
    path('food/', Food.as_view(), name = 'food'),
    path('register/',RegisteUsers.as_view() , name = 'register'),
    path('login/',LoginUsers.as_view(),name = 'login'),
    path ('logout/', logout_user, name = 'logout'),
    path ('user/',UsersHome.as_view(),name = 'usershome'),
    path('order/', OrderingProgram.as_view(),name = 'ordering'),
    #homepage user
]
