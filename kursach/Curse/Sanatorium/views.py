from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView,TemplateView,DetailView

from .forms import AddUsersForm, RegisterUserForm, LoginUserForm, OrderingForm
from .models import *
from .utils import DataMixin

# Create your views here.

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


class OrderingProgram(DataMixin, CreateView):
    model = Order
    form_class = OrderingForm
    template_name = 'sanatorium/order.html'
    success_url = '/orders/'

    def form_valid(self, form):
        form.instance.user_id = self.request.user
        return super().form_valid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        return {**context,**c_def}

class RegisteUsers (DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'sanatorium/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('mainpage')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title = "Регистрация")
        return {**context,**c_def}


class LoginUsers (DataMixin,LoginView):
    form_class = LoginUserForm
    template_name = 'sanatorium/login.html'

    def get_success_url(self):
        return reverse_lazy('usershome')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return {**context, **c_def}



class UsersHome(DataMixin,TemplateView):
    template_name = 'sanatorium/user_lobby.html'
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        return {**context,**c_def}
def logout_user(request):
    logout(request)
    return redirect('login')

"""class UserInfoAdd(DataMixin,CreateView):"""