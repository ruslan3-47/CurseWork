from lib2to3.fixes.fix_input import context

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import *
# Create your views here.


menu = [{'title' : "Главная страница", 'url' : "MainPage"},
        {'title' : "Комнаты", 'url' : "Rooms"},
        {'title' : "Бронь", 'url' : "Booking"},
        {'title' : "О нас", 'url' : "About"}
        ]
def index(request):
    return render(request,'sanatorium/index.html',{'menu':menu, 'title':"Новая Заря"})

def about(request):
    return render(request,'sanatorium/about.html',{'menu':menu,'title':"Новая Заря"})

def rooms(request):
    type_room = Type.objects.all()
    room = Room.objects.all()
    context = {
        'menu': menu,
        'title': "Новая Заря",
        "type": type_room,
        "room": room,
    }
    return render(request,'sanatorium/rooms.html',context=context)

def booking(request):
    return render(request,'sanatorium/booking.html',{'menu':menu, 'title':"Новая Заря"})


