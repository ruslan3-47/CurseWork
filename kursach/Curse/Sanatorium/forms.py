from cProfile import label

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import *
class OrderingForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['program_name','room_id','date_in','date_out']
        widgets = {
            'date_in': forms.DateInput(attrs={'type':'date'}),
            'date_out':forms.DateInput(attrs={'type':'date'}),
        }
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['room_id'].queryset = Room.objects.all()
        self.fields['program_name'].queryset = Program.objects.all()

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин')
    email = forms.EmailField(label='E-mail')
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label="Логин", widget=forms.TextInput())
    password = forms.CharField(label='Пароль', widget= forms.PasswordInput())


class ProfileEdit(forms.ModelForm):
    class Meta:
        model = Users
        fields = ["first_name","last_name",'middle_name', 'birth_date']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type':'date'})
        }

class EditUser(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['first_name','last_name','middle_name','birth_date']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'})
        }


class EditProgram(forms.ModelForm):
    class Meta:
        model = Program
        fields = ['name','price','description','briefly_description','date']


class EditRoom(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['type','image','slug']


class EditType(forms.ModelForm):
    class Meta:
        model = Type
        fields = ['name','price','description','brify_description']

class CreateUser(forms.ModelForm):
    class Meta:
        model = Users
        fields = "__all__"
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'})
        }


class CreateProgram(forms.ModelForm):
    class Meta:
        model = Program
        fields = "__all__"


class CreateRoom(forms.ModelForm):
    class Meta:
        model = Room
        fields = "__all__"


class CreateType(forms.ModelForm):
    class Meta:
        model = Type
        fields = "__all__"