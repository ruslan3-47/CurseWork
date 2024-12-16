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

    def save(self, commit=True):
        user = super().save(commit = False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label="Логин", widget=forms.TextInput())
    password = forms.CharField(label='Пароль', widget= forms.PasswordInput())


class ProfileEdit(forms.ModelForm):
    first_name = forms.CharField(label='Имя', max_length=30, required=False)
    last_name = forms.CharField(label='Фамилия', max_length=30, required=False)
    class Meta:
        model = Users
        fields = ['middle_name', 'birth_date']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type':'date'})
        }

    def __init__(self, *args, **kwargs):
            self.user = kwargs.pop('user', None)
            super().__init__(*args, **kwargs)

            if self.user:
                self.fields['first_name'].initial = self.user.first_name
                self.fields['last_name'].initial = self.user.last_name


    def save(self,commit = True):
        instance = super().save(commit=False)
        if self.user:
            self.user.first_name = self.cleaned_data.get('first_name', self.user.first_name)
            self.user.last_name = self.cleaned_data.get('last_name', self.user.last_name)
            self.user.save()
        if commit:
            instance.save()
        return instance