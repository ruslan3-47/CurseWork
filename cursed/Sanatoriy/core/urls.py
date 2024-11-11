from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('rooms/',rooms),
    path('select_room/<slug:type_rooms>/',select_room),
    path('about/',about)
]