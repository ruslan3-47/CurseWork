from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Users


class AddUsersForm(forms.ModelForm):

    class Meta:
        model = Users
        fields = ['last_name','first_name','middle_name','email','birth_date','date_in','date_out', 'is_in','program','room']

    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['room'].empty_label = "не выбрана"
        self.fields['program'].empty_label = "не выбрана"


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