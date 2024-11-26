from django import forms
from .models import Program
from .models import Room
from .models import Users


class AddUsersForm(forms.ModelForm):

    class Meta:
        model = Users
        fields = ['last_name','first_name','middle_name','email','birth_date','date_in','date_out', 'is_in','program','room']

    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['room'].empty_label = "не выбрана"
        self.fields['program'].empty_label = "не выбрана"


