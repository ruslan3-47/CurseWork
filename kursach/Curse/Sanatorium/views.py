from django.contrib.auth import logout, login

from django.contrib.auth.views import LoginView
from django.shortcuts import get_object_or_404,redirect

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, TemplateView, DetailView, UpdateView


from .forms import *
from .models import *
from .utils import DataMixin
from .filter import *
# Create your views here.

class Homepage(DataMixin,TemplateView):
    template_name = 'sanatorium/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Проверяем, аутентифицирован ли пользователь
        if self.request.user.is_authenticated:
            try:
                # Пытаемся получить объект Users, связанный с текущим пользователем
                user_profile = Users.objects.get(user=self.request.user)
            except Users.DoesNotExist:
                # Если объект не существует, устанавливаем user_profile в None
                user_profile = None
        else:
            # Если пользователь не аутентифицирован, user_profile также None
            user_profile = None

        # Передаем user_profile в контекст
        c_def = self.get_user_context(user_profile=user_profile)
        return {**context, **c_def}


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
    paginate_by = 3

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
        return redirect('mainpage')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title = "Регистрация")
        return {**context,**c_def}


class LoginUsers (DataMixin,LoginView):
    form_class = LoginUserForm
    template_name = 'sanatorium/login.html'

    def get_success_url(self):
         return reverse_lazy('mainpage')

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
        user_profile = get_object_or_404(Users, user=self.request.user)
        c_def = self.get_user_context(user_profile = user_profile)
        return {**context,**c_def}


class UserInfoAdd(DataMixin,UpdateView):
    model = Users
    form_class = ProfileEdit
    template_name = 'sanatorium/editProfile.html'
    success_url = reverse_lazy('usershome')
    def get_object(self, queryset=None):
        return self.request.user.users

class AdminViews(DataMixin,ListView):
    template_name = "sanatorium/admiinpage.html"
    model = Users
    context_object_name = "user"
    paginate_by = 20
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = self.get_queryset()

        us_filter = UserFilter(self.request.GET,queryset)
        pr_filter = ProgramFilter(self.request.GET, queryset=Program.objects.all(),prefix="program")
        rm_filter = RoomFilter(self.request.GET, queryset=Room.objects.all(),prefix="room")
        tp_filter = TypeFilter(self.request.GET, queryset=Type.objects.all(),prefix="type")
        c_def = self.get_user_context(
            program = pr_filter.qs,
            room = rm_filter.qs,
            type = tp_filter.qs,
            us_filter= us_filter,
            pr_filter=pr_filter,
            rm_filter=rm_filter,
            tp_filter = tp_filter)
        return {**context,**c_def}

    def get_queryset(self):
        queryset = super().get_queryset()
        us_filter = UserFilter(self.request.GET,queryset)
        return us_filter.qs

class EditUser(DataMixin,UpdateView):
    model = Users
    form_class = EditUser
    template_name = "sanatorium/EditUser.html"
    success_url =  reverse_lazy('admin')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        return {**context, **c_def}


class EditProgram(DataMixin,UpdateView):
    model = Program
    form_class = EditProgram
    template_name = "sanatorium/EditProgram.html"
    success_url = reverse_lazy('admin')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        return {**context, **c_def}


class EditRoom(DataMixin, UpdateView):
    model = Room
    form_class = EditRoom
    template_name = "sanatorium/EditRoom.html"
    success_url = reverse_lazy('admin')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        return {**context, **c_def}


class EditType(DataMixin, UpdateView):
    model = Type
    form_class = EditType
    template_name = "sanatorium/EditType.html"
    success_url = reverse_lazy('admin')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        return {**context, **c_def}


class CreateUser(DataMixin,CreateView):
    model = Users
    form_class = CreateUser
    template_name = "sanatorium/createuser.html"
    success_url =  reverse_lazy('admin')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        return {**context, **c_def}

    def form_valid(self, form):
        user = form.save()
        Users.objects.create(user = user)
        return redirect('admin')

class CreateProgram(DataMixin,CreateView):
    model = Program
    form_class = CreateProgram
    template_name = "sanatorium/createprogram.html"
    success_url = reverse_lazy('admin')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        return {**context, **c_def}

    def form_valid(self, form):
        program = form.save()
        Program.objects.create(program = program)
        return redirect('admin')


class CreateRoom(DataMixin, CreateView):
    model = Room
    form_class = CreateRoom
    template_name = "sanatorium/createroom.html"
    success_url = reverse_lazy('admin')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        return {**context, **c_def}

    def form_valid(self, form):
        room = form.save()
        Room.objects.create(room = room)
        return redirect('admin')


class CreateType(DataMixin, CreateView):
    model = Type
    form_class = CreateType
    template_name = "sanatorium/creattype.html"
    success_url = reverse_lazy('admin')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        return {**context, **c_def}

    def form_valid(self, form):
        type = form.save()
        Type.objects.create(type = type)
        return redirect('admin')