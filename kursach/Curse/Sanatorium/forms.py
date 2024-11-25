from django import forms
from .models import Program
from .models import Room

class AddUsersForm(forms.Form):
    last_name = forms.CharField(label = "Фамилия", max_length=50)
    first_name = forms.CharField(label='Имя', max_length=50)
    middle_name = forms.CharField(label='Отчество', max_length=50)
    email = forms.EmailField(label='e-mail')
    birth_date = forms.DateField(label='Дата рождения')
    is_in = forms.BooleanField(label='Заселен', required=False, initial=True)
    program = forms.ModelChoiceField(label='Программа',queryset=Program.objects.all(), empty_label='Не выбрана')
    room = forms.ModelChoiceField(label = 'Комната', queryset=Room.objects.all(), empty_label='Не выбрана')