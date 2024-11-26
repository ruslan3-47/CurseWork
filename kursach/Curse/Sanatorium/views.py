
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.views.generic import ListView

from .forms import AddUsersForm
from .models import *

# Create your views here.


menu = [{'title': "Главная страница", 'url': "mainpage"},
        {'title': "Номера", 'url': "rooms"},
        {'title': "Программы", 'url': "programs"},
        {'title': "О нас", 'url': "about"},
        {'title':"Питание", 'url': "food" },
        {'title': "Зарегистрировать", 'url': "addusers"}
        ]


def index(request):
    return render(request, 'sanatorium/index.html', {'menu': menu, 'title': "Новая Заря"})


def about(request):
    return render(request, 'sanatorium/about.html', {'menu': menu, 'title': "Новая Заря"})


class Rooms(ListView):
    model = Room
    template_name = 'sanatorium/rooms.html'
    context_object_name = 'room'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Новая Заря'
        context['menu'] = menu
        context['type'] = Type.objects.all()
        return context

    def get_queryset(self):
        return Room.objects.filter(is_order = False)

def booking(request):
    program = Program.objects.all()
    context = {
        'menu': menu,
        'title': "Новая Заря",
        'program': program
    }
    return render(request, 'sanatorium/booking.html', context = context)


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

def show_program(request,program_slug):
    program = get_object_or_404(Program,slug = program_slug)
    descprog = Program.objects.all()
    context = {
        'menu': menu,
        'title': "Новая Заря",
        "program_slug": program,
        "program": descprog,
    }
    return render(request,'sanatorium/show_program.html', context = context)

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

def food(request):
    return render(request, 'sanatorium/food.html',{'title': 'Новая Заря','menu':menu})