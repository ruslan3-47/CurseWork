from django.urls import path

from Sanatoriy.urls import urlpatterns
from views import index,groups

urlpatterns = [
    path('',index),
    path('groups/',groups),
]