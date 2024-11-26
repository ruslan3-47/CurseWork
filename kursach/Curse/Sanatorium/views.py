
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from .forms import AddUsersForm
from .models import *

# Create your views here.


menu = [{'title': "Главная страница", 'url': "mainpage"},
        {'title': "Комнаты", 'url': "rooms"},
        {'title': "Бронь", 'url': "booking"},
        {'title': "О нас", 'url': "about"},
        {'title': "Зарегистрировать", 'url': "addusers"}
        ]


def index(request):
    return render(request, 'sanatorium/index.html', {'menu': menu, 'title': "Новая Заря"})


def about(request):
    return render(request, 'sanatorium/about.html', {'menu': menu, 'title': "Новая Заря"})


def rooms(request):
    type_room = Type.objects.all()
    room = Room.objects.all()
    context = {
        'menu': menu,
        'title': "Новая Заря",
        "type": type_room,
        "room": room,
    }
    return render(request, 'sanatorium/rooms.html', context=context)


def booking(request):
    return render(request, 'sanatorium/booking.html', {'menu': menu, 'title': "Новая Заря"})


def show_room(request, room_slug):
    room = get_object_or_404(Room, slug=room_slug)
    decsroom = Room.objects.all()
    context = {
        'menu': menu,
        'title': "Новая Заря",
        "room_slug": room,
        "room": decsroom,

    }
    return render(request, 'sanatorium/show_room.html', context=context)


def addusers(request):
    if request.method == 'POST':
        form = AddUsersForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            try:
                Users.objects.create(**form.cleaned_data)
                return redirect('mainpage')
            except:
                form.add_error(None, "Ошибка!")
    else:
        form = AddUsersForm()
    return render(request, 'sanatorium/addusers.html', {'title': 'Новая Заря', 'form': form})

