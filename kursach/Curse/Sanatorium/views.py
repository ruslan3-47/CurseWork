
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from django.views.generic import TemplateView
from django.views.generic import DetailView
from matplotlib.style.core import context

from .forms import AddUsersForm
from .models import *
from .utils import DataMixin

# Create your views here.


menu = [{'title': "Главная страница", 'url': "mainpage"},
        {'title': "Номера", 'url': "rooms"},
        {'title': "Программы", 'url': "programs"},
        {'title': "О нас", 'url': "about"},
        {'title':"Питание", 'url': "food" },
        {'title': "Зарегистрировать", 'url': "addusers"}
        ]

class Homepage(DataMixin,TemplateView):
    template_name = 'sanatorium/index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        return {**context,**c_def}


class About(DataMixin,TemplateView):
    template_name = 'sanatorium/about.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        return {**context,**c_def}


class Rooms(DataMixin,ListView):
    model = Room
    template_name = 'sanatorium/rooms.html'
    context_object_name = 'room'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(type =Type.objects.all() )
        return {**context,**c_def}

    def get_queryset(self):
        return Room.objects.filter(is_order = False)

class Program_html(DataMixin,ListView):
    model = Program
    template_name = 'sanatorium/booking.html'
    context_object_name = 'program'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def =  self.get_user_context()
        return {**context,**c_def}


class ShowRoom(DataMixin,DetailView):
    model = Room
    template_name = 'sanatorium/show_room.html'
    context_object_name = 'room'

    def get_object(self, queryset=None):
        return get_object_or_404(Room,slug = self.kwargs['room_slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(desc_room = Room.objects.all())
        return {**context,**c_def}


class Show_program(DataMixin,DetailView):
    model = Program
    template_name = 'sanatorium/show_program.html'
    context_object_name = 'program'

    def get_object(self, queryset=None):
        return get_object_or_404(Program, slug =self.kwargs['program_slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(desc_program = Program.objects.all())
        return {**context,**c_def}


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


class Food(DataMixin,TemplateView):
    template_name = 'sanatorium/food.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        return {**context,**c_def}
