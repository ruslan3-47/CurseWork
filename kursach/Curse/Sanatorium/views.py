from django.contrib.auth import logout, login, get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, TemplateView, DetailView, UpdateView

from .forms import AddUsersForm, RegisterUserForm, LoginUserForm, OrderingForm, ProfileEdit
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
    success_url = reverse_lazy('mainpage')

    def form_valid(self, form):
        form.instance.user_id = self.request.user.users
        self.calculate_total_cost(form)
        response = super().form_valid(form)
        self.object = form.instance
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(total_cost = self.object.price if self.object else None)
        return {**context,**c_def}

    def calculate_total_cost(self, form):
        # Извлекаем данные из формы
        program_name = form.cleaned_data['program_name']
        room_id = form.cleaned_data['room_id']
        date_in = form.cleaned_data['date_in']
        date_out = form.cleaned_data['date_out']
        # Вычисляем количество дней
        date = (date_out - date_in).days
        # Вычисляем общую стоимость
        program_price = program_name.price
        room_price = room_id.type.price
        total_cost = program_price + (room_price * date)
        # Устанавливаем общую стоимость на экземпляре формы
        form.instance.total_cost = total_cost

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class RegisteUsers (DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'sanatorium/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        Users.objects.create(user = user)
        login(self.request, user)
        return redirect('addinfo')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title = "Регистрация")
        return {**context,**c_def}


class LoginUsers (DataMixin,LoginView):
    form_class = LoginUserForm
    template_name = 'sanatorium/login.html'

    def get_success_url(self):
        user = self.request.user
        try:
            user_profile = Users.objects.get(user=user)
            if user_profile.first_name and user_profile.last_name and user_profile.middle_name and user_profile.birth_date and user_profile.email:
                return reverse_lazy('mainpage')
            else:
                return reverse_lazy('addinfo')
        except Users.DoesNotExist:
            return reverse_lazy('addinfo')


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return {**context, **c_def}

def logout_user(request):
    logout(request)
    return redirect('login')


class UsersHome(DataMixin,TemplateView):
    template_name = 'sanatorium/user_lobby.html'
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        return {**context,**c_def}


class UserInfoAdd(DataMixin,UpdateView):
    model = Users
    form_class = ProfileEdit
    template_name = 'sanatorium/addmoreinfo.html'
    success_url = reverse_lazy('usershome')
    def get_object(self, queryset=None):
        return self.request.user.users