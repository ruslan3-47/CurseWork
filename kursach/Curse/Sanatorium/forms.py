from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import *


class AddUsersForm(forms.ModelForm):

    class Meta:
        model = Users
        fields = ['last_name','first_name','middle_name','email','birth_date']

    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['room'].empty_label = "не выбрана"
        self.fields['program'].empty_label = "не выбрана"

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
        fields = ['first_name','last_name', 'middle_name', 'birth_date']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type':'date'})
        }

        def __init__(self, *args, **kwargs):
            self.user = kwargs.pop('user', None)
            super().__init__(*args, **kwargs)

        def save(self,commit = True):
            instance = super().save(commit=False)
            if self.user:
                instance.email = self.user.email
            if commit:
                instance.save()
            return instance